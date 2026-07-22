import pandas as pd


# These are the exact features used during ML model training.
MODEL_FEATURES = [
    "Store_ID",
    "Product_ID",
    "Price",
    "Year",
    "Month",
    "Day",
    "DayOfWeek",
    "Quarter",
    "IsWeekend",
    "Product_Name_Keyboard",
    "Product_Name_Laptop",
    "Product_Name_Monitor",
    "Product_Name_Mouse",
    "Product_Name_Printer",
    "Category_Accessories",
    "Category_Electronics",
]


def prepare_forecast_input(
    store_id: int,
    product_id: int,
    price: float,
    date: str,
    product_name: str,
    category: str,
) -> pd.DataFrame:

    # Convert the date string into a pandas datetime object.
    parsed_date = pd.to_datetime(date)

    # Create the basic numerical features.
    data = {
        "Store_ID": store_id,
        "Product_ID": product_id,
        "Price": price,
        "Year": parsed_date.year,
        "Month": parsed_date.month,
        "Day": parsed_date.day,
        "DayOfWeek": parsed_date.dayofweek + 1,
        "Quarter": parsed_date.quarter,
        "IsWeekend": 1 if parsed_date.dayofweek >= 5 else 0,
    }

    # Normalize the product name.
    normalized_product = product_name.strip().lower()

    # Add one-hot encoded product features.
    data["Product_Name_Keyboard"] = (
        1 if normalized_product == "keyboard" else 0
    )

    data["Product_Name_Laptop"] = (
        1 if normalized_product == "laptop" else 0
    )

    data["Product_Name_Monitor"] = (
        1 if normalized_product == "monitor" else 0
    )

    data["Product_Name_Mouse"] = (
        1 if normalized_product == "mouse" else 0
    )

    data["Product_Name_Printer"] = (
        1 if normalized_product == "printer" else 0
    )

    # Normalize the category.
    normalized_category = category.strip().lower()

    # Add one-hot encoded category features.
    data["Category_Accessories"] = (
        1 if normalized_category == "accessories" else 0
    )

    data["Category_Electronics"] = (
        1 if normalized_category == "electronics" else 0
    )

    # Create a DataFrame with exactly the model's expected columns.
    dataframe = pd.DataFrame([data])

    # Reorder the columns to exactly match the training order.
    dataframe = dataframe[MODEL_FEATURES]

    return dataframe