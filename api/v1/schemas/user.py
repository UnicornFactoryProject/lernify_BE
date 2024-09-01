from pydantic import BaseModel, EmailStr, StringConstraints, model_validator
from email_validator import validate_email, EmailNotValidError
from typing import Annotated, Dict
import dns.resolver


def is_valid_mx_record(domain: str):
    """ checks if the domain has a valid MX record
    """
    try:
        # Try to resolve the MX record for the domain
        mx_records = dns.resolver.resolve(domain, 'MX')
        return True if mx_records else False
    except dns.resolver.NoAnswer:
        return False
    except dns.resolver.NXDOMAIN:
        return False
    except Exception:
        return False


class CreateUserSchema(BaseModel):
    """Schema to create a user"""

    email: EmailStr
    password: Annotated[
        str, StringConstraints(
            min_length=8,
            max_length=64,
            strip_whitespace=True
        )
    ]
    first_name: Annotated[
        str, StringConstraints(
            min_length=3,
            max_length=30,
            strip_whitespace=True
        )
    ]
    last_name: Annotated[
        str, StringConstraints(
            min_length=3,
            max_length=30,
            strip_whitespace=True
        )
    ]

    @model_validator(mode='before')
    @classmethod
    def validate_password(cls, values: Dict[str, str]) -> Dict[str, str]:
        """ Validates password
        """
        password = values.get('password')
        special_chars = "!@#$%^&*()-+"

        # password requirement checks
        if not any(char.islower() for char in password):
            raise ValueError("password must include at least one lowercase character")
        if not any(char.isupper() for char in password):
            raise ValueError("password must include at least one uppercase character")
        if not any(char.isdigit() for char in password):
            raise ValueError("password must include at least one digit")
        if not any(char in special_chars for char in password):
            raise ValueError("password must include at least one special character")
        return values

    @model_validator(mode='before')
    @classmethod
    def validate_email(cls, values: Dict[str, str]) -> Dict[str, str]:
        """validates email
        """
        email = values.get('email')
        try:
            email = validate_email(email, check_deliverability=True)
            if email.domain.count(".com") > 1:
                raise EmailNotValidError("Email address contains multiple '.com' endings.")
            if not is_valid_mx_record(email.domain):
                raise ValueError('Email is invalid')
        except EmailNotValidError as exc:
            raise ValueError(exc) from exc
        except Exception as exc:
            raise ValueError(exc) from exc
        
        return values

        
class LoginUserSchema(BaseModel):
    """Schema to create a user"""

    email: EmailStr
    password: Annotated[
        str, StringConstraints(
            min_length=8,
            max_length=64,
            strip_whitespace=True
        )
    ]

class ForgotPasswordSchema(BaseModel):
    """Forgot password schema
    """
    email: EmailStr

class PasswordResetSchema(BaseModel):
    token: str
    new_password: str

    @model_validator(mode='before')
    @classmethod
    def validate_password(cls, values: Dict[str, str]) -> Dict[str, str]:
        """ Validates password
        """
        password = values.get('new_password')
        special_chars = "!@#$%^&*()-+"

        # password requirement checks
        if not any(char.islower() for char in password):
            raise ValueError("password must include at least one lowercase character")
        if not any(char.isupper() for char in password):
            raise ValueError("password must include at least one uppercase character")
        if not any(char.isdigit() for char in password):
            raise ValueError("password must include at least one digit")
        if not any(char in special_chars for char in password):
            raise ValueError("password must include at least one special character")
        return values