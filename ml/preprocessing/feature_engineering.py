import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "cleaned_sales.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "features.csv"

df = pd.read_csv(INPUT_FILE)

df["Date"] = pd.to_datetime(df["Date"])

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["DayOfWeek"] = df["Date"].dt.dayofweek
df["Quarter"] = df["Date"].dt.quarter
df["IsWeekend"] = df["DayOfWeek"].isin([5, 6]).astype(int)

print(df.head())

df.to_csv(OUTPUT_FILE, index=False)

print("\nFeature engineering completed successfully!")
print(f"Saved to: {OUTPUT_FILE}")