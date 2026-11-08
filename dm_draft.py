from models.outreach import OutreachDraft
import json
from models.buisness_profile import BusinessProfile
from models.research import ResearchReport
from models.lead_model import Qualification
from models.outreach import OutreachStrategy
from services.gemini_services import GeminiService
from google.genai import types


def build_outreach_prompt(
    business_details: BusinessProfile,
    prospect: ResearchReport,
    qualification: Qualification,
    strategy: OutreachStrategy,
):
    # Lists ko strings mein convert karo (f-string ke bahar)
    services_str = "\n".join(business_details.services)
    industries_str = "\n".join(business_details.target_industries)
    prospect_services_str = "\n".join([s.service for s in prospect.services_offered])
    reasons_str = ", ".join(qualification.reasons)

    prompt = f"""
MARKEVIAN:
- Services: {services_str}
- Target market: {business_details.target_market}
- Target industries: {industries_str}

PROSPECT:
- Overview: {prospect.business_overview.description}
- Key services: {prospect_services_str}
- Target customers: {prospect.target_customers.description}

QUALIFICATION:
- Score: {qualification.score}/100
- Priority: {qualification.priority}
- Reasons: {reasons_str}

OUTREACH STRATEGY:
- Channel: {strategy.channel}
- Reasoning: {strategy.reasoning}

INSTRUCTIONS:
Write a short, personalized outreach email (100-150 words) for the prospect above.

RULES:
- NO generic filler ("I hope this email finds you well")
- NO fabricated claims — use evidence from the research
- Reference specific things from the prospect's website
- Explain why Markavian is relevant to THEM specifically
- Clear call-to-action (e.g., 15-min call)
- Professional but conversational tone

Return JSON with:
- subject: email subject line
- body: email body
- personalization_evidence: list of specific things you referenced
- objective: what this email aims to achieve
- next_step: recommended follow-up action
"""
    return prompt



def build_outreach_draft(prompt , gemini: GeminiService) -> OutreachDraft:

    response = gemini.generate_response(
        prompt=prompt ,
        config= types.GenerateContentConfig(
            response_mime_type="application/json" ,
            response_schema=OutreachDraft
        )
    )
    return OutreachDraft(**json.loads(response.text))

