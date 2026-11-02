from pydantic import BaseModel
from typing import List




class BusinessProfile(BaseModel):

    business_name : str
    services : List[str]
    target_market : str
    target_industries : List[str]