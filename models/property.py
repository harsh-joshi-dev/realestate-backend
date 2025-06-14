from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime

class Property(BaseModel):
    property_title: str = Field(..., example="3BHK Luxury Apartment in Bandra West")
    
    condition: Literal["New", "Old"] = Field(..., example="New")  # New or Old
    category: str = Field(..., example="Villa")  # Office, Villa, Apartment, Plot, etc.
    
    square_feet: int = Field(..., example=1800)
    rate: int = Field(..., example=12000000)  # Total cost or rent amount

    location: str = Field(..., example="Bandra West, Mumbai")
    
    furnishing_status: Literal["Furnished", "Semi-Furnished", "Unfurnished"] = Field(..., example="Furnished")
    
    parking_options: List[Literal["Car", "Bike", "None"]] = Field(..., example=["Car", "Bike"])
    parking_capacity: Optional[List[str]] = Field(None, example=["1 Car", "2 Bikes"])

    # Rental Specific (can be null for sale)
    allowed_for: Optional[List[Literal["Family", "Bachelor"]]] = Field(None, example=["Family"])
    family_members_allowed: Optional[int] = Field(None, example=5)

    availability_status: str = Field(..., example="Available")  # Available, Sold, Rented, Upcoming, etc.
    listed_by: Optional[str] = Field(None, example="agent_123")  # Or "owner_001"
    created_by: Optional[str] = Field(None, example="admin_001")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
