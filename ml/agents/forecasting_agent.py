import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "saved_models" / "random_forest.pkl"


class ForecastingAgent:

    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def forecast(self, input_data):
        prediction = self.model.predict(input_data)
        return prediction


if __name__ == "__main__":

    DATA_DIR = BASE_DIR / "data" / "processed"

    X_test = pd.read_csv(DATA_DIR / "X_test.csv")

    agent = ForecastingAgent()

    sample = X_test.iloc[[0]]

    prediction = agent.forecast(sample)

    print("Predicted Sales:", prediction[0])