import requests
from typing import List
from bs4 import BeautifulSoup
from urllib.parse import urlparse

main_links = ['https://www.goodfirms.co/social-media-marketing/india',
              'https://www.digitalvidya.com/blog/social-media-agency/', 
              'https://www.designrush.com/agency/social-media-marketing/in',
                'https://www.nicodigital.com/social-media/social-media-marketing-agency-india/', 'https://clutch.co/in/agencies/social-media-marketing',
                  'https://brandshark.com/social-media-marketing-agencies-in-india/', 'https://www.f6s.com/companies/social-media-marketing/india/co',
                    'https://www.sortlist.com/social-media/india-in', 
              'https://technewscast.io/india/social-media-marketing/']

bad_list = ["facebook", "instagram", "linkedin", "twitter", "goodfirms", 
 "clutch", "designrush", "sortlist", "f6s", "digitalvidya", 
 "brandshark", "technewscast", "nicodigital" , "google" ,"openai", "x.com", "grok", "chatgpt", "youtube", "youtu.be"]

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
            response = requests.get(link , timeout=10)
            if response.status_code == 200:
                html_data.append(response.text)
        except requests.exceptions.RequestException:
            continue

    for html in html_data:
        soup = BeautifulSoup(html , "html.parser")

        for p in soup.find_all("a"):
            href = p.get("href")
            href : bytes

            if not href:
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



result = get_directory_data(main_links)
print(result)


