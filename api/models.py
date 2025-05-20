from typing import Optional

from pydantic import BaseModel


class AccountMeta(BaseModel):
    id: int
    name: str
    phone: str
    email: str
    address: str
    hotel_type: str

class RoomType(BaseModel):
    id: int
    name: str
    description: Optional[str]
    adults: int
    children: int
    photos: Optional[list[dict]] = None
    name_ru: Optional[str]
    name_en: Optional[str]

class PlanModel(BaseModel):
    id: int
    name: str
    description: Optional[str]
    booking_guarantee_sum: float
    booking_guarantee_unit: str
    cancellation_rules: Optional[str]
    cancellation_deadline: str
