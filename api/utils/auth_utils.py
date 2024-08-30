from passlib.context import CryptContext

# Initialize the CryptContext with your hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Function to hash a password
    """
    hashed_password = pwd_context.hash(password)
    return hashed_password