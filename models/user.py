from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal
from datetime import datetime

class User(BaseModel):
    name: str = Field(..., example="Rahul Sharma")
    phone: str = Field(..., example="+91-9876543210")
    email: Optional[EmailStr] = Field(None, example="rahul@example.com")
    user_type: Optional[Literal["buyer", "owner", "broker"]] = Field("buyer")
    preferred_location: Optional[str] = Field(None, example="Pune")
    password: Optional[str] = Field(None, example="mypassword123")  # add password here
    created_at: datetime = Field(default_factory=datetime.utcnow)
