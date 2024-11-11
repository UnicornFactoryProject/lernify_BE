from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.session import SessionLocal
from app.models.user import User
from app.models.password_reset import PasswordReset
from app.schemas.auth import SignIn, TokenResponse, EmailSchema, CodeVerificationSchema, ResetPasswordSchema
from app.core.security import verify_password, hash_password  # Assuming you have a password hashing utility
from app.core.jwt import create_access_token
from app.utils.email import send_email  # Define an email sending utility

router = APIRouter()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# User sign-in route
@router.post("/signin", response_model=TokenResponse)
def sign_in(credentials: SignIn, db: Session = Depends(get_db)):
    # Retrieve user from the database
    user = db.query(User).filter(User.email == credentials.email).first()
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Create JWT token if authentication is successful
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# Request password reset route
@router.post("/request-reset/")
def request_password_reset(data: EmailSchema, db: Session = Depends(get_db)):
    # Generate a random 6-digit code and store it in the DB
    verification_code = "123456"  # Replace with actual random code generation
    reset_request = PasswordReset(email=data.email, code=verification_code)
    db.add(reset_request)
    db.commit()
    # Send email with verification code
    send_email(to=data.email, subject="Password Reset Code", body=f"Your code is {verification_code}")
    return {"message": "A verification code has been sent to your email."}

# Verify password reset code route
@router.post("/verify-code/")
def verify_code(data: CodeVerificationSchema, db: Session = Depends(get_db)):
    # Check if the code exists and is still valid
    reset_request = db.query(PasswordReset).filter_by(email=data.email, code=data.code, is_used=False).first()
    if not reset_request or reset_request.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Invalid or expired code.")
    return {"message": "Code verified successfully. Proceed to reset your password."}

# Reset password route
@router.post("/reset-password/")
def reset_password(data: ResetPasswordSchema, db: Session = Depends(get_db)):
    if data.new_password != data.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match.")
    # Verify the reset code again
    reset_request = db.query(PasswordReset).filter_by(email=data.email, code=data.code, is_used=False).first()
    if not reset_request or reset_request.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Invalid or expired code.")
    # Reset password and mark code as used
    user = db.query(User).filter_by(email=data.email).first()
    user.hashed_password = hash_password(data.new_password)  # Ensure password hashing is applied here
    reset_request.is_used = True
    db.commit()
    return {"message": "Password reset successful."}
