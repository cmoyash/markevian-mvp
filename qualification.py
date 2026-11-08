from models.research import ResearchReport
from models.buisness_profile import BusinessProfile
from models.lead_model import Qualification




def qualify_lead(report: ResearchReport , business_config: BusinessProfile) -> Qualification:
    score = 0
    reasons = []
    missing = []

    # Industry [30]
    industry = business_config.industry_keywords
    overview_text = report.business_overview.description.lower()
    if any(kw in overview_text for kw in industry):
        score += 30
        reasons.append("Industry Match")
    else:
        missing.append("Industry not matched")


    #Location [20]
    cities = business_config.target_cities
    offices = report.contact_channels.office_locations

    has_target_city = False

    for office in offices:
        office_location = office.address.lower()

        if any(city in  office_location for city in cities):
            has_target_city = True
            break
    if has_target_city:
        score += 20
        reasons.append("Target City Match")
    else:
        missing.append("Target City Missing")

    #activeBusiness [20]

    if len(report.services_offered) > 0:
        score += 20
        reasons.append("Active Business")
    else:
        missing.append("Business is not active")


    #Service Match [20]

    service_match = False

    for services in report.services_offered:
        if any(kw in services.service.lower() for kw in business_config.industry_keywords):
            service_match = True
            break 

    if service_match:
        score += 20
        reasons.append("Service Matched")
    else:
        missing.append("Service not matched")

    #Contact [10]

    if len(report.contact_channels.emails) > 0:
        score += 10
        reasons.append("Found Contact")
    else:
        missing.append("contact not found")


    if score >= 70 :
        priority = "High"
    elif score >= 50 :
        priority = "Medium"
    else:
        priority = "Low"


    return Qualification(
        score=score ,
        priority=priority ,
        reasons=reasons ,
        missing=missing
    )

    
    