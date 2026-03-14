import pandas as pd

def export_products(products, file_path="data/products.csv"):
    df = pd.DataFrame(products)
    df.to_csv(file_path, index=False)

def export_category_summary(products, file_path="data/category_summary.csv"):
    df = pd.DataFrame(products)
    summary = df.groupby(["subcategory"]).agg(
        total_products=("title", "count"),
        avg_price=("price", "mean"),
        min_price=("price", "min"),
        max_price=("price", "max"),
        missing_descriptions=("description", lambda x: x.isna().sum()),
    ).reset_index()
    summary.to_csv(file_path, index=False)