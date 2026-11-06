from ddgs import DDGS
from typing import List
import requests

from pathlib import Path
from models.buisness_profile import BusinessProfile
from typing import Any
import json


def load_business_config(file: Any) -> dict:
    file_path = Path(file)

    if not file_path.exists():
        raise FileNotFoundError(f"file not found: {file_path}")

    with open(file_path , "r" , encoding="utf-8") as f:
        data = json.load(f)
    return data




def web_search(query: str):
    results = []

    with DDGS() as ddgs:
        # Direct text() method call karo
        search_results = ddgs.text(query)
        
        if search_results:
            for r in search_results:
                results.append({
                    "title": r.get("title", ""),
                    "url": r.get("href", ""),
                    "snippet": r.get("body", "")
                })
    
    return results


def dedublication(search_results: List):
    seen_url = set()
    unique_searach = []

    for r in search_results:
        url = r.get('url')

        if url in seen_url:
            continue

        seen_url.add(url)
        unique_searach.append(r)
    return unique_searach




data = load_business_config("knowledgebase_data/business_data.json")
profile = BusinessProfile(**data)

def generate_query(profile: BusinessProfile):
    industry = profile.target_industries[0]
    return f"{industry} in {profile.target_market}"

query = generate_query(profile)
main_result = web_search(query)
data = dedublication(main_result)


#extract part


final_links = []
def extract_directory_links(data):
    for r in data:
        final_links.append(r["url"])
    return final_links

main_data = extract_directory_links(data)
print(main_data)


# def extract_agency_links(links: List[str]):

#     for link in links:
#         try:
#             main_html = requests.get(link)
#             if main_html:
#                 return main_html



