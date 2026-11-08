from pydantic import BaseModel
from typing import Optional , List





class Lead(BaseModel):
    name : str
    industry : str
    website : Optional[str] = None
    source : Optional[str] = None


class Qualification(BaseModel):
    score : int
    priority :  str
    reasons : List[str]
    missing : List[str] 
