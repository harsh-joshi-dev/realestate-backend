from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Literal
from datetime import datetime

class UpdateUserTypeRequest(BaseModel):
    phone: str
    password: str
    new_user_type: Literal["buyer", "owner", "broker"]