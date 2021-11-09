# Python
from uuid import UUID
from datetime import date
from typing import Optional

from pydantic import (
    BaseModel,
    EmailStr,
    Field
)

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=1,
        max_length=50
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birdh_date: Optional[date] = Field(...)

class Tweet(BaseModel):
    pass