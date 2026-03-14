from .utils import safe_request, join_url

def parse_product_list(listing_page_url):
    """Extract product links from a listing page."""
    soup = safe_request(listing_page_url)
    links = []
    for a in soup.select(".title"):  # product links
        url = join_url(listing_page_url, a.get("href"))
        links.append(url)
    return links

def _slug_to_title(slug: str) -> str:
    # e.g. "computers" -> "Computers", "touch" -> "Touch"
    return slug.replace("-", " ").title()


def parse_product_detail(product_url, category, subcategory, page_number):
    """Extract product data from detail page."""
    soup = safe_request(product_url)
    title = soup.select("h4")[1].text.strip() if len(soup.select("h4")) > 1 else ""
    price = soup.select_one(".price").text.strip().replace("$", "") if soup.select_one(".price") else ""
    description = soup.select_one(".description").text.strip() if soup.select_one(".description") else ""
    reviews = soup.select_one(".ratings p").text.strip() if soup.select_one(".ratings p") else ""
    # Important details
    specs = [li.text.strip() for li in soup.select(".specs li")]

    return {
        "category": _slug_to_title(category.split("/")[-1]),
        "subcategory": _slug_to_title(subcategory.split("/")[-1]),
        "title": title,
        "price": float(price) if price else None,
        "url": product_url,
        "description": description,
        "reviews": reviews,
        "specs": ", ".join(specs),
        "page": page_number,
    }