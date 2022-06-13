#python
from typing import Optional
from uuid import UUID
from datetime import date

#pydantic
from pydantic import (BaseModel, EmailStr, Field)


class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr  = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=25
    )
class User(BaseModel):
   
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=80,
        
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=80,
        
    )
    bird_date: Optional[date] = Field(default=None)

class Tweet(BaseModel):
    pass