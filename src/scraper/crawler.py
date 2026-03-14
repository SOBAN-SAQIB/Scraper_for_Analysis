import requests
from bs4 import BeautifulSoup
from .utils import join_url, safe_request

BASE_URL = "https://webscraper.io/test-sites/e-commerce/static"

def get_categories():
    """Return list of category URLs."""
    soup = safe_request(BASE_URL)
    categories = []
    for a in soup.select(".sidebar-nav a"):  # sidebar links
        url = join_url(BASE_URL, a.get("href"))
        categories.append(url)
    return categories

def get_subcategories(category_url):
    """Return list of subcategory URLs."""
    soup = safe_request(category_url)
    subcategories = []
    for a in soup.select(".subcategory a"):
        url = join_url(BASE_URL, a.get("href"))
        subcategories.append(url)
    return subcategories

def get_paginated_links(subcategory_url):
    """Return all paginated listing pages for a subcategory."""
    soup = safe_request(subcategory_url)
    pages = [subcategory_url]
    for a in soup.select(".pagination a"):
        url = join_url(BASE_URL, a.get("href"))
        if url not in pages:
            pages.append(url)
    return pages