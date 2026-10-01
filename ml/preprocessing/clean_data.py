import pandas as pd
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = BASE_DIR / "data" / "raw" / "sales_dataset_250.csv"

PROCESSED_DATA = BASE_DIR / "data" / "processed" / "cleaned_sales.csv"
df = pd.read_csv(RAW_DATA)

print(df.head())
print("\nDataset Information")
print(df.info())

print("\nShape")
print(df.shape)
print("\nMissing Values")
print(df.isnull().sum())
before = len(df)

df.drop_duplicates(inplace=True)

after = len(df)

print(f"\nDuplicates Removed: {before - after}")
df["Date"] = pd.to_datetime(df["Date"])
print(df.dtypes)
df = df.sort_values("Date")
df.reset_index(drop=True, inplace=True)
df.to_csv(PROCESSED_DATA, index=False)

print("\nCleaned dataset saved successfully!")
print(PROCESSED_DATA)
