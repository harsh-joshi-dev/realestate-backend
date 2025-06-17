from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime

class Customer(BaseModel):
    full_name: str = Field(..., example="Ramesh Gupta")
    caste: Optional[str] = Field(None, example="Brahmin")
    contact_number: int = Field(..., example=9876543210)

    preferred_bhk: Optional[str] = Field(None, example="2BHK")
    residential_property_type: Optional[str] = Field(None, example="Apartment")  # Apartment, Villa, etc.
    commercial_property_type: Optional[str] = Field(None, example="Office")      # Office, Shop, etc.

    intent: Optional[str] = Field(..., example=["Rent", "Buy"])
    property_condition: Optional[str] = Field(..., example=["New", "Resale"])

    furnished_status: Optional[str] = Field(..., example=["Furnished", "Unfurnished"])
    parking_options: Optional[str] = Field(..., example=["Car Parking", "Bike Parking"])

    budget_min: Optional[int] = Field(None, example=2500000)
    budget_max: Optional[int] = Field(None, example=5000000)

    special_requirements: Optional[str] = Field(None, example="Near hospital, top floor, garden view")
    preferred_area: Optional[List[str]] = Field(None, example="South Mumbai, Andheri East")

    waiting_period: Optional[str] = Field(None, example="1 Month")
    
    city_name: Optional[str] = Field(None, example="Delhi")

    # For rental preferences
    preferred_tenant_type: Optional[str] = Field(None, example=["Bachelor", "Married"])
    family_members_count: Optional[int] = Field(None, example=4)

    # Meta
    created_by: Optional[str] = Field(None, example="admin_user_001")
    assigned_to: Optional[str] = Field(None, example="agent_007")  # Or 'self' if assigned to self
    lead_source: Optional[str] = Field(None, example="Google Ads")  # Website, Referral, etc.
    status: Optional[str] = Field(None, example="Interested")       # Follow Up, Not Interested, Closed, etc.

    added_on: datetime = Field(default_factory=datetime.utcnow)
