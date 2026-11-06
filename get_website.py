import requests
from bs4 import BeautifulSoup
from typing import List
from urllib.parse import urlparse




main_links = ['https://www.goodfirms.co/social-media-marketing/india',
              'https://www.digitalvidya.com/blog/social-media-agency/', 
              'https://www.designrush.com/agency/social-media-marketing/in',
                'https://www.nicodigital.com/social-media/social-media-marketing-agency-india/', 'https://clutch.co/in/agencies/social-media-marketing',
                  'https://brandshark.com/social-media-marketing-agencies-in-india/', 'https://www.f6s.com/companies/social-media-marketing/india/co',
                    'https://www.sortlist.com/social-media/india-in', 
              'https://technewscast.io/india/social-media-marketing/']


def dedublicate(result_list: List):
    seen_links = set()
    uniqe_links = []

    for link in result_list:
        if link in seen_links:
            continue

        seen_links.add(link)
        uniqe_links.append(link)
    return uniqe_links





def get_directory_data(links: List[str]):
    html_data = []
    for link in links:
        try:
            response =  requests.get(link)
            if response.status_code == 200:
                html_data.append(response.text)
        except requests.exceptions.RequestException:
            continue

    final_links = []

    for html in html_data:
        soup = BeautifulSoup(html , "html.parser")

        for r in soup.find_all("a"):
            href = r.get("href") 
            
            if not href:
                continue

            if not href.startswith("http"):
                continue

            parsed = urlparse(href)
            netloc = parsed.netloc
            

            if any(bad in netloc for bad in ["facebook", "instagram", "linkedin", "twitter", "goodfirms", 
 "clutch", "designrush", "sortlist", "f6s", "digitalvidya", 
 "brandshark", "technewscast", "nicodigital" , "google" ,"openai", "x.com", "grok", "chatgpt", "youtube", "youtu.be"]):
                continue



            if netloc.endswith(".com") or netloc.endswith(".in") or netloc.endswith(".co")  or netloc.endswith(".io"):
                clean_url = f"{parsed.scheme}://{parsed.netloc}"
                final_links.append(clean_url)
    return dedublicate(final_links)




result = get_directory_data(main_links)
print(result)
for link in result:
    print(link)
    