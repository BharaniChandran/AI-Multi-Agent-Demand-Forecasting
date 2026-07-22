import pandas as pd
import joblib
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "processed"

MODEL_DIR = BASE_DIR / "saved_models"

MODEL_DIR.mkdir(exist_ok=True)

# Load training data
X_train = pd.read_csv(DATA_DIR / "X_train.csv")
y_train = pd.read_csv(DATA_DIR / "y_train.csv")

# Convert target to 1D
y_train = y_train.squeeze()

print("Training Features Shape:", X_train.shape)
print("Training Target Shape:", y_train.shape)

# Create model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Save model
joblib.dump(
    model,
    MODEL_DIR / "random_forest.pkl"
)

print("\nModel trained successfully!")
print("Saved at:", MODEL_DIR / "random_forest.pkl")