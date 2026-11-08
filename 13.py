from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin



# def fetch_url(url):

#     try:
#         response = requests.get(url , timeout=10)
#         if response.status_code == 200:
#             return response.text
#         else:
#             return f"Failed due to {response.status_code}"
#     except requests.exceptions.RequestException as e:
#         print(f"Error Found {e}")
#         return None
    



# def fetch_html(html , base):

#     pages = {}

#     soup = BeautifulSoup(html , "html.parser")

#     for p in soup.find_all("a"):
#         href = p.get("href")

#         if not href or not isinstance(href , str):
#             continue


#         section = href.lower()

#         if "about" in section and "about" not in pages:
#             pages["about"] = urljoin(base , href)

#         if "service" in section and "service" not in pages:
#             pages["services"] = urljoin(base , href)

#         if  "contact" in section and "contact" not in pages:
#             pages["contact"] = urljoin(base , href)
       
#     return pages



# html = """
# <nav>Menu</nav>
# <h1>Title</h1>
# <p>Content</p>
# <footer>Footer</footer>
# """

# soup = BeautifulSoup(html , "html.parser")

# for tag in soup.find_all(["nav" , "footer"]):
#     tag.decompose()

# print(soup.get_text())


# html = "<p>Hello</p><p>World</p><p>Test</p>"

# soup = BeautifulSoup(html , "html.parser")


# print(soup.get_text())
# print("==========")
# print(soup.get_text(separator=" "))



# text = "Hello    World\n\nTest   Python"



# print(text.split())
# print(60 * "=")
# print(" ".join(text.split()))


# html = """
# <nav>Menu</nav>
# <h1>Social Panga</h1>
# <p>We are a creative agency.</p>
# <script>alert('x')</script>
# <footer>Footer</footer>
# """

# def extract_text(html):

#     soup = BeautifulSoup(html , "html.parser")

#     for tag in soup.find_all(["nav" , "header" , "footer" , "script" , "style"]):
#         tag.decompose()

#     clean_text = soup.get_text(separator=" ")
#     return (" ").join(clean_text.split())



# result = extract_text(html)
# print(result)




def collect_agency_data(agency_url):
    try:
        response = requests.get(agency_url)
        if response.status_code == 200:
            html = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e} ")
        return None

    tags = ["header" , "footer" , "script" , "style" , "nav"]
    soup = BeautifulSoup(html , "html.parser")

    for tag in soup.find_all(tags):
        tag.decompose()
    
    clean_html = soup.get_text(separator=" ")
    homepage_text = (" ").join(clean_html.split())



    


# collect_agency_data("https://socialpanga.com")