import requests
from bs4 import BeautifulSoup

def join_url(base, url):
    if url.startswith("http"):
        return url
    return base.rstrip("/") + "/" + url.lstrip("/")

def safe_request(url):
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return BeautifulSoup(r.text, "html.parser")
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return BeautifulSoup("", "html.parser")


# utils.py
def remove_duplicates(products):
    seen = set()
    result = []
    for p in products:
        if p["url"] not in seen:
            seen.add(p["url"])
            result.append(p)
    return result