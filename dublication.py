from models.lead_model import Lead
from typing import List

# raw = [
#     {"name": "Mumbai Agency A", "url": "mumbaiagency.com"},
#     {"name": "Delhi Agency B", "url": "delhiagency.com"}
# ]

# def convert_to_lead(raw , industry) -> List:
#     results = []

#     for r in raw:
#         leads = Lead(
#             name=r["name"] ,
#             industry=industry ,
#             website=r["url"]  ,
#             source="search"
#         )
#         results.append(leads)
#     return results

# data = convert_to_lead(raw , "digital marketing")

# for lead in data:
#     print(f"Name: {lead.name} | Industry: {lead.industry} | Website: {lead.website}")



# def deduplicate(raw):

#     seen_url = set()
#     unique_results = []

#     for r in raw:
#         url = r.get("url")
#         if not url or url in seen_url:
#             continue

#         seen_url.add(url)
#         unique_results.append(r)

#     return unique_results






# raw = [
#     {"url": "https://a.com", "name": "A1"},
#     {"url": "https://a.com", "name": "A2"},  # Duplicate
#     {"url": "https://b.com", "name": "B1"}
# ]

# unique_raw = deduplicate(raw)
# print(unique_raw)





leads = [
    Lead(name="Agency A", website="https://a.com", industry="Marketing"),
    Lead(name="Agency A again", website="https://a.com", industry="Marketing"), # Duplicate
    Lead(name="Agency B", website="https://b.com", industry="Marketing")
]

def dedublicate_leads(leads: List[Lead]) -> List[Lead]:
    seen_websites = set()
    unique_leads = []

    for lead in leads:
        website = lead.website

        if website in seen_websites:
            continue

        seen_websites.add(website)
        unique_leads.append(lead)
    return unique_leads



data = dedublicate_leads(leads)

for main_lead in data:
    print(f"Name: {main_lead.name} | Website: {main_lead.website}")