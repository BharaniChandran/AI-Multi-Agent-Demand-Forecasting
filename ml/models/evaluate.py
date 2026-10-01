import pandas as pd
import joblib
from pathlib import Path

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "processed"

MODEL_DIR = BASE_DIR / "saved_models"

# Load test data
X_test = pd.read_csv(DATA_DIR / "X_test.csv")
y_test = pd.read_csv(DATA_DIR / "y_test.csv").squeeze()

# Load trained model
model = joblib.load(
    MODEL_DIR / "random_forest.pkl"
)

# Make predictions
predictions = model.predict(X_test)

# Calculate metrics
mae = mean_absolute_error(y_test, predictions)

rmse = mean_squared_error(
    y_test,
    predictions
) ** 0.5

r2 = r2_score(
    y_test,
    predictions
)

# Display metrics
print("\nModel Evaluation")
print("-" * 30)
print(f"MAE : {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²  : {r2:.4f}")

# Save prediction results
results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
})

results.to_csv(
    DATA_DIR / "prediction_results.csv",
    index=False
)

# Save metrics
with open(DATA_DIR / "model_metrics.txt", "w") as file:
    file.write("Random Forest Evaluation\n")
    file.write("========================\n")
    file.write(f"MAE : {mae:.2f}\n")
    file.write(f"RMSE: {rmse:.2f}\n")
    file.write(f"R²  : {r2:.4f}\n")

print("\nEvaluation completed successfully!")