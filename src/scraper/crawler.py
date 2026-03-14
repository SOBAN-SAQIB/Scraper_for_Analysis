import requests
from bs4 import BeautifulSoup
from .utils import join_url, safe_request

BASE_URL = "https://webscraper.io/test-sites/e-commerce/static"

def get_categories():
    """Return list of category URLs."""
    return [
        "https://webscraper.io/test-sites/e-commerce/static/computers",
        "https://webscraper.io/test-sites/e-commerce/static/phones"
    ]

def get_subcategories(category_url):
    """Return list of subcategory URLs."""
    if "computers" in category_url:
        return [
            "https://webscraper.io/test-sites/e-commerce/static/computers/laptops",
            "https://webscraper.io/test-sites/e-commerce/static/computers/tablets"
        ]
    elif "phones" in category_url:
        return [
            "https://webscraper.io/test-sites/e-commerce/static/phones/touch"
        ]
    return []

def get_paginated_links(subcategory_url):
    """Return all paginated listing pages for a subcategory.

    The pagination control sometimes shows only a subset of pages (e.g., 2-10, 19-20),
    so we infer the maximum page number and generate the full range.
    """

    soup = safe_request(subcategory_url)

    # Find the largest page number in the pagination links
    max_page = 1
    for a in soup.select(".pagination a"):
        text = a.get_text(strip=True)
        if text.isdigit():
            max_page = max(max_page, int(text))

    pages = [subcategory_url]
    for page in range(2, max_page + 1):
        pages.append(f"{subcategory_url}?page={page}")

    return pages