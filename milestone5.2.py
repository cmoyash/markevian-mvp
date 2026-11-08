import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from typing import List , Dict
from services.gemini_services import GeminiService
from google.genai import types
from models.research import ResearchReport
gemini = GeminiService()

bad_list = [
    "facebook", "instagram", "linkedin", "twitter", "goodfirms",
    "clutch", "designrush", "sortlist", "f6s", "digitalvidya",
    "brandshark", "technewscast", "nicodigital", "google", "openai",
    "x.com", "grok", "chatgpt", "youtube", "youtu.be"
]


# ---------- Directory scraping ----------

def dedublication(all_links):
    seen_links = set()
    unique_links = []
    for link in all_links:
        if link in seen_links:
            continue
        seen_links.add(link)
        unique_links.append(link)
    return unique_links


def get_directory_data(directory_links: List[str]):
    html_data = []
    final_links = []

    for link in directory_links:
        try:
            response = requests.get(link, timeout=10)
            if response.status_code == 200:
                html_data.append(response.text)
        except requests.exceptions.RequestException:
            continue

    for html in html_data:
        soup = BeautifulSoup(html, "html.parser")
        for p in soup.find_all("a"):
            href = p.get("href")
            if not href or not isinstance(href, str):
                continue
            if not href.startswith("http"):
                continue
            parsed = urlparse(href)
            netloc = parsed.netloc
            if any(bad in netloc for bad in bad_list):
                continue
            if netloc.endswith(".com") or netloc.endswith(".in") or netloc.endswith(".co") or netloc.endswith(".io"):
                clean_url = f"{parsed.scheme}://{parsed.netloc}"
                final_links.append(clean_url)

    return dedublication(final_links)


# ---------- Page fetch ----------

def fetch_url(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error Found {e}")
        return None


# ---------- Relevant pages dhoondho ----------

def find_relevant_pages(html, base):
    pages = {}
    soup = BeautifulSoup(html, "html.parser")

    for p in soup.find_all("a"):
        href = p.get("href")
        if not href or not isinstance(href, str):
            continue
        section = href.lower()

        if "about" in section and "about" not in pages:
            pages["about"] = urljoin(base, href)
        if "service" in section and "services" not in pages:
            pages["services"] = urljoin(base, href)
        if "contact" in section and "contact" not in pages:
            pages["contact"] = urljoin(base, href)

    return pages


# ---------- Text extract ----------

def extract_text(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(["nav", "header", "footer", "script", "style"]):
        tag.decompose()
    clean_text = soup.get_text(separator=" ")
    return " ".join(clean_text.split())


# ---------- Agency data collect ----------

def collect_agency_data(agency_url):
    result = {}

    # Step 1: Homepage fetch
    homepage_html = fetch_url(agency_url)
    if not homepage_html:
        return result

    # Step 2: Homepage ka text
    result["homepage"] = extract_text(homepage_html)

    # Step 3: Relevant pages dhoondho
    pages = find_relevant_pages(homepage_html, agency_url)

    # Step 4: Har page ka text
    for key, url in pages.items():
        page_html = fetch_url(url)
        if page_html:
            result[key] = extract_text(page_html)

    return result

# data = collect_agency_data("https://socialpanga.com")
# print(data.keys())
# for k, v in data.items():
#     print(k, "→", len(v), "chars")




def trim_text(text, limit=2000):
    return text[:limit] if text else ""

# print(len(trim_text("a" * 5000)))   # 2000
# print(len(trim_text("hello")))      # 5
# print(trim_text(""))                # "" (empty, crash nahi)
# print(trim_text(None))              # "" (empty, crash nahi)



def build_research_prompt(ageny_name: str , data: Dict):

    agency_line = f"Research the following agency : {ageny_name}"

    page_block = []
    for key , text in data.items():
        block = f"------{key.upper()}-----\n{trim_text(text , 5000)}"
        page_block.append(block)

    page_text = ("\n\n").join(page_block)
    instructions = (
    "Based on the above information, extract:\n"
    "- Business overview (with evidence)\n"
    "- Services offered: EACH service as a separate object with its OWN evidence\n"
    "- Target customers (with evidence)\n"
    "- Contact channels: emails (list), office locations (city + address)\n\n"
    "Return JSON matching the schema.\n"
    "Every claim MUST have evidence from the text above.\n"
    "For services, list each service SEPARATELY with its specific evidence."
)
    prompt = f"{agency_line}\n\n{page_text}\n\n{instructions}"
    return prompt

data = collect_agency_data("https://socialpanga.com")
prompt = build_research_prompt("Social Panga", data)

result  = gemini.generate_response(
    prompt=prompt ,
    config=types.GenerateContentConfig(
        response_mime_type="application/json" , 
        response_schema=ResearchReport
    )
)

print(result.text)