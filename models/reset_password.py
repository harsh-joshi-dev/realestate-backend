from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class ResetPasswordRequest(BaseModel):
    phone: str = Field(..., example="+91-9876543210")
    new_password: str = Field(..., example="newpassword123")
