from pydantic import BaseModel, Field, field_validator
import re


class User(BaseModel):
    email: str
    password: str = Field(..., min_length=8, max_length=255)

    @field_validator('email')
    def validate_email(cls, value):
        email_regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if not email_regex.match(value):
            raise ValueError('Invalid email address')
        return value
