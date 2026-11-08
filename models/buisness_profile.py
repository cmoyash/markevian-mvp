from pydantic import BaseModel
from typing import List


class IdealCustomer(BaseModel):
    has_existing_clients: bool
    has_an_active_business: bool


class BusinessProfile(BaseModel):
    business_name: str
    services: List[str]
    target_market: str
    target_industries: List[str]
    industry_keywords: List[str]
    target_cities: List[str]
    ideal_customer: IdealCustomer
    goals: List[str]