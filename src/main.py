from scraper.crawler import get_categories, get_subcategories, get_paginated_links
from scraper.parsers import parse_product_list, parse_product_detail
from scraper.exporters import export_products, export_category_summary
from scraper.utils import remove_duplicates

def main():
    all_products = []
    categories = get_categories()
    for cat_url in categories:
        subcategories = get_subcategories(cat_url)
        for sub_url in subcategories:
            pages = get_paginated_links(sub_url)
            for i, page in enumerate(pages, 1):
                product_links = parse_product_list(page)
                for link in product_links:
                    product = parse_product_detail(link, cat_url, sub_url, i)
                    all_products.append(product)

    # Calculate duplicates removed per category/subcategory before deduplication
    # so we can report the count even if we remove them later.
    from collections import Counter

    url_pairs = [(p["category"], p["subcategory"], p["url"]) for p in all_products]
    dup_counter = Counter()
    seen = set()
    for cat, sub, url in url_pairs:
        key = (cat, sub, url)
        if key in seen:
            dup_counter[(cat, sub)] += 1
        else:
            seen.add(key)

    all_products = remove_duplicates(all_products)
    export_products(all_products)
    export_category_summary(all_products, duplicates_removed=dup_counter)
    print("Scraping finished. CSVs generated in /data folder.")


if __name__ == "__main__":
    main()