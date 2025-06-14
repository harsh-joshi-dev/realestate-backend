from pydantic import BaseModel, EmailStr, Field
from typing import Literal

class UserRegister(BaseModel):
    full_name: str = Field(..., example="Ramesh Gupta")
    email: EmailStr = Field(..., example="ramesh@example.com")
    password: str = Field(..., min_length=6)
    role: Literal["admin", "team_member", "user"] = Field(..., example="admin")

class UserLogin(BaseModel):
    email: EmailStr
    password: str
