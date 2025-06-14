from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import List, Optional, Literal
from datetime import datetime

class ContractorDetails(BaseModel):
    contractor_name: str = Field(..., example="ABC Builders Pvt Ltd")
    contractor_contact: str = Field(..., example="+91-9876543210")

class Property(BaseModel):
    property_title: str = Field(..., example="3BHK Luxury Apartment in Bandra West")
    
    condition: Literal["New", "Old"] = Field(..., example="New")
    category: str = Field(..., example="Villa")
    
    square_feet: int = Field(..., example=1800)
    rate: int = Field(..., example=12000000)

    location: str = Field(..., example="Bandra West, Mumbai")
    
    furnishing_status: Literal["Furnished", "Semi-Furnished", "Unfurnished"] = Field(..., example="Furnished")
    
    parking_options: List[Literal["Car", "Bike", "None"]] = Field(..., example=["Car", "Bike"])
    parking_capacity: Optional[List[str]] = Field(None, example=["1 Car", "2 Bikes"])

    allowed_for: Optional[List[Literal["Family", "Bachelor"]]] = Field(None, example=["Family"])
    family_members_allowed: Optional[int] = Field(None, example=5)

    availability_status: str = Field(..., example="Available")
    listed_by: Optional[str] = Field(None, example="agent_123")
    created_by: Optional[str] = Field(None, example="admin_001")

    owner_name: str = Field(..., example="Mr. Sharma")

    contractor_details: Optional[ContractorDetails] = None

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None

    @model_validator(mode="after")
    def validate_contractor_requirement(self) -> "Property":
        if self.condition == "Old" and not self.contractor_details:
            raise ValueError("contractor_details are required for old properties")
        return self
