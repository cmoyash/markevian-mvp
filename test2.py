from models.research import ResearchReport
import json
from qualification import qualify_lead
from models.buisness_profile import BusinessProfile
from models.outreach import OutreachStrategy
from outreach_decide_tool import decide_outreach_channel

lead_file = "knowledgebase_data/social_panga.json"

with open(lead_file , "r") as f:
    lead_data = json.load(f)

bizz_file = "knowledgebase_data/business_data.json"

with open(bizz_file , "r") as f:
    bizz_data = json.load(f)


report = ResearchReport(**lead_data)
business_config = BusinessProfile(**bizz_data)


result = qualify_lead(report=report , business_config=business_config)
strategy = decide_outreach_channel(report=report , qualification=result)

print(f"Channel: {strategy.channel}")
print(f"Reasoning: {strategy.reasoning}")
print(f"Next Action: {strategy.next_action}")