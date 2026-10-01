import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "processed" / "features.csv"
OUTPUT_DIR = BASE_DIR / "data" / "processed"

df = pd.read_csv(INPUT_FILE)

# Target variable
y = df["Sales"]

# Feature columns
X = df.drop(columns=["Sales"])

# Remove Date column
X = X.drop(columns=["Date"])

# Convert categorical columns into numeric values
X = pd.get_dummies(
    X,
    columns=["Product_Name", "Category"]
)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Save datasets
X_train.to_csv(OUTPUT_DIR / "X_train.csv", index=False)
X_test.to_csv(OUTPUT_DIR / "X_test.csv", index=False)

y_train.to_csv(OUTPUT_DIR / "y_train.csv", index=False)
y_test.to_csv(OUTPUT_DIR / "y_test.csv", index=False)

print("Training Features:", X_train.shape)
print("Testing Features :", X_test.shape)
print("Training Target :", y_train.shape)
print("Testing Target  :", y_test.shape)

print("\nDataset successfully split!")