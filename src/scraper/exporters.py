import os

import pandas as pd


def _ensure_writable(path: str) -> bool:
    """Return True if the given path can be written to (or removed).

    If the file exists but is locked by another process, this returns False.
    """

    if not os.path.exists(path):
        return True

    try:
        os.remove(path)
        return True
    except PermissionError:
        # Try relaxing permissions and retry once.
        try:
            os.chmod(path, 0o666)
            os.remove(path)
            return True
        except PermissionError:
            return False


def export_products(products, file_path="data/products.csv"):
    can_write = _ensure_writable(file_path)
    df = pd.DataFrame(products)

    if not can_write:
        alt_path = file_path + ".new.csv"
        print(f"WARNING: Could not overwrite '{file_path}' (file locked). Writing to '{alt_path}' instead.")
        file_path = alt_path

    df.to_csv(file_path, index=False)

def export_category_summary(products, duplicates_removed=None, file_path="data/category_summary.csv"):
    can_write = _ensure_writable(file_path)
    df = pd.DataFrame(products)

    if df.empty or "subcategory" not in df.columns or "category" not in df.columns:
        header = [
            "category",
            "subcategory",
            "total_products",
            "avg_price",
            "min_price",
            "max_price",
            "missing_descriptions",
            "duplicates_removed",
        ]
        empty_df = pd.DataFrame(columns=header)

        if not can_write:
            alt_path = file_path + ".new.csv"
            print(f"WARNING: Could not overwrite '{file_path}' (file locked). Writing summary to '{alt_path}' instead.")
            file_path = alt_path

        empty_df.to_csv(file_path, index=False)
        return

    # Compute duplicates removed per (category, subcategory) if not provided.
    if duplicates_removed is None:
        dup_df = df.groupby(["category", "subcategory"]).apply(
            lambda g: len(g) - g["url"].nunique()
        )
        duplicates_removed = dup_df.to_dict()

    summary = df.groupby(["category", "subcategory"]).agg(
        total_products=("title", "count"),
        avg_price=("price", "mean"),
        min_price=("price", "min"),
        max_price=("price", "max"),
        missing_descriptions=("description", lambda x: (x == "").sum()),
    ).reset_index()

    # Round prices for readability (matches expected summary format)
    summary[["avg_price", "min_price", "max_price"]] = summary[["avg_price", "min_price", "max_price"]].round(2)

    # Attach duplicates_removed column (default 0)
    summary["duplicates_removed"] = summary.apply(
        lambda row: int(duplicates_removed.get((row["category"], row["subcategory"]), 0)),
        axis=1,
    )

    if not can_write:
        alt_path = file_path + ".new.csv"
        print(f"WARNING: Could not overwrite '{file_path}' (file locked). Writing summary to '{alt_path}' instead.")
        file_path = alt_path

    summary.to_csv(file_path, index=False)