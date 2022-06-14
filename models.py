#python
from typing import Optional
from uuid import UUID, uuid4
from datetime import (date, datetime)

#pydantic
from pydantic import (BaseModel, EmailStr, Field)


#models User

class UserBase(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    email: EmailStr  = Field(...)

class User(UserBase):
   
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
    birth_date: Optional[date] = Field(default=None)

class UserLogin(UserBase ):
    password: str = Field(
        ...,
        min_length=8,
        max_length=25
    )  

class UserRegister(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=25
    )  

#models Tweets
class Tweet(BaseModel):
    tweet_id : UUID = Field(...)
    content : str = Field(
        ...,
        min_length=1,
        max_length=256,
    )
    created_at: datetime = Field(default=datetime.now())
    update_at: Optional[datetime] = Field(default=datetime.now())
    by: User= Field(...)