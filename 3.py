from urllib.parse import urlparse



p = urlparse("https://www.adlift.in/services?page=2")





url = "https://webfx.com/about/"



urls = [
    "https://abc.com",
    "https://abc.com/about",
    "https://abc.in/services/seo",
    "https://abc.co",
    "https://abc.io/pricing",
    "https://facebook.com/abc",
]


for r in urls:
    p = urlparse(r).netloc

    if p.endswith("com") or p.endswith("in") or p.endswith("io") or p.endswith("co"):
        print(f"Pass: {r}")
    else:
        print(f"Fail: {r}")



