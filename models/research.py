from pydantic import BaseModel
from typing import List




class BusinessOverview(BaseModel):
    description : str
    evidence :  List[str]

class Service(BaseModel):
    service : str
    evidence : List[str]

class TargetCustomers(BaseModel):
    description : str
    evidence : List[str]

class OfficeLocation(BaseModel):
    city : str
    address : str

class Email(BaseModel):
    email_name : str
    email : str

class ContactChannels(BaseModel):
    emails : List[Email]
    office_locations : List[OfficeLocation]
    evidence : List[str]

class ResearchReport(BaseModel):
    business_overview : BusinessOverview
    services_offered : List[Service]
    target_customers : TargetCustomers
    contact_channels : ContactChannels
