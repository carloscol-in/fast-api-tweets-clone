# Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional

from pydantic import (
    BaseModel,
    EmailStr,
    Field
)

class PasswordMixin(BaseModel):
    password: str = Field(
        ...,
        min_length=1,
        max_length=64
    )

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Joe"
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Doe"
    )
    birth_date: Optional[date] = Field(...)

class UserLogin(PasswordMixin, UserBase):
    pass

class UserRegister(PasswordMixin, User):
    pass

