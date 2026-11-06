import requests





def fetch_url(url):
    try:
        response = requests.get(url , timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error found: {e}")
        return None


html = fetch_url("https://socialpanga.com")
print(html)





