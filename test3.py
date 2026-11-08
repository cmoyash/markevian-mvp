from dm_draft import build_outreach_prompt
from models.buisness_profile import BusinessProfile
import json
from models.research import ResearchReport
from models.lead_model import Qualification
from qualification import qualify_lead
from outreach_decide_tool import decide_outreach_channel
from dm_draft import build_outreach_draft
from services.gemini_services import GeminiService

gemini = GeminiService()


bizz_file = "knowledgebase_data/business_data.json"
with open(bizz_file , "r") as f:
    bizz_data = json.load(f)
business_details = BusinessProfile(**bizz_data)

prospect_file = "knowledgebase_data/social_panga.json"
with open(prospect_file , "r") as f:
    prospect_data = json.load(f)
prospect = ResearchReport(**prospect_data)

qualification = qualify_lead(
    report=prospect ,
    business_config=business_details
)

strategy = decide_outreach_channel(
    report=prospect ,
    qualification=qualification
)


prompt = build_outreach_prompt(
    business_details=business_details ,
    prospect=prospect ,
    qualification=qualification ,
    strategy=strategy
)

draft = build_outreach_draft(prompt=prompt , gemini=gemini)

print(f"Subject: {draft.subject}")
print(f"\nBody:\n{draft.body}")
print(f"\nEvidence: {draft.personalization_evidence}")
print(f"Objective: {draft.objective}")
print(f"Next Step: {draft.next_step}")

