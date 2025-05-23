from pydantic import BaseModel
from typing import Optional

# Base schema to include common fields
class UserBase(BaseModel):
    username: str
    password: str

# Schema for creating a user (includes user_id)
class UserCreate(UserBase):
    pass

# Schema for updating a user (optional fields)
class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None

# Schema that includes the response model for user
class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True
