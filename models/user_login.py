from pydantic import BaseModel, Field

class UserLogin(BaseModel):
    phone: str = Field(..., example="9876543210")
    password: str = Field(..., example="mypassword")
