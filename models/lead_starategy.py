from pydantic import BaseModel
from typing import List





class LeadStarategy(BaseModel):

    target_industry :  str
    location :  str
    signals_to_research : List[str]
    qualification_criteria : List[str]

    