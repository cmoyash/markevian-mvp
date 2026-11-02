from pydantic import BaseModel
from typing import Optional





class Lead(BaseModel):
    name : str
    industry : str
    website : Optional[str] = None
    source : Optional[str] = None

    