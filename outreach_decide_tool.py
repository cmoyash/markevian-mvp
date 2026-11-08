from models.research import ResearchReport
from models.lead_model import Qualification
from models.outreach import OutreachStrategy


def decide_outreach_channel(report:ResearchReport , qualification: Qualification) -> OutreachStrategy:


    if qualification.priority.lower() == "low":
        return OutreachStrategy(
            channel="manual_research" ,
            reasoning="Due to low lead priority" ,
            next_action="Skip outreach or manual review"
        )

    emails = report.contact_channels.emails
    if not emails:
        return OutreachStrategy(
            channel="manual_research" ,
            reasoning="No email found" ,
            next_action="No email found"
            )

    for email in emails:
        if "business" in email.email_name.lower():
            return OutreachStrategy(
                channel="email" ,
                reasoning=f"Business Email: {email.email}" ,
                next_action=f"Send email to {email.email}"
            )

    first = emails[0]
    return OutreachStrategy(
            channel="email" , 
            reasoning=f"Email: {first.email}" , 
            next_action=f"Email to {first.email}"
        )
    