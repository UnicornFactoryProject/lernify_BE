from pydantic import BaseModel, EmailStr, constr

# Sign-in schema
class SignIn(BaseModel):
    email: EmailStr
    password: str

# Token response schema
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

# Step 1: Request Reset Schema
class EmailSchema(BaseModel):
    email: EmailStr

# Step 2: Verify Code Schema
class CodeVerificationSchema(BaseModel):
    email: EmailStr
    code: str

# Step 3: Reset Password Schema
class ResetPasswordSchema(BaseModel):
    email: EmailStr
    code: str
    new_password: constr(min_length=8)
    confirm_password: constr(min_length=8)
