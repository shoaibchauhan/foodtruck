from typing import Optional

from pydantic import BaseModel


class DataIn(BaseModel):
    Latitude: float
    Longitude: float


class DataOut(BaseModel):
    locationid: int
    Applicant: Optional[str]
    FacilityType: Optional[str]
    LocationDescription: Optional[str]
    Address: Optional[str]
    Status: Optional[str]
    FoodItems: Optional[str]
    Latitude: Optional[float]
    Longitude: Optional[float]
