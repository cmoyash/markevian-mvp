from pydantic import BaseModel
from typing import List , Literal , Optional


class OutreachStrategy(BaseModel):

    channel : Literal["email", "linkedin", "instagram", "facebook", "manual_research"]
    reasoning :  str
    next_action :  str


class OutreachDraft(BaseModel):
    channel : Literal["email", "linkedin", "instagram", "facebook", "manual_research"]
    subject : Optional[str] = None
    body :  str
    personalization_evidence : List[str]
    objective : str
    next_step : str

