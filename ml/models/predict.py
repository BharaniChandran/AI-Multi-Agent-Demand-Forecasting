import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "saved_models" / "random_forest.pkl"

INPUT_FILE = BASE_DIR / "data" / "processed" / "sample_input.csv"

OUTPUT_FILE = BASE_DIR / "data" / "processed" / "sample_predictions.csv"

# Load model
model = joblib.load(MODEL_PATH)

# Read sample input
sample = pd.read_csv(INPUT_FILE)

# Predict
predictions = model.predict(sample)

# Save predictions
sample["Predicted_Sales"] = predictions

sample.to_csv(OUTPUT_FILE, index=False)

print(sample)