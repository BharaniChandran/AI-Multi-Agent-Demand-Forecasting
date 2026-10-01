import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PREDICTION_FILE = BASE_DIR / "data" / "processed" / "prediction_results.csv"
ANOMALY_FILE = BASE_DIR / "data" / "processed" / "anomaly_results.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "recommendations.csv"


class RecommendationAgent:

    def generate_recommendation(
        self,
        predicted_sales,
        anomaly
    ):

        if anomaly == -1:
            return "Investigate unusual sales pattern"

        elif predicted_sales >= 70:
            return "Increase inventory"

        elif predicted_sales >= 30:
            return "Maintain current stock"

        else:
            return "Reduce inventory"


if __name__ == "__main__":

    prediction_df = pd.read_csv(PREDICTION_FILE)
    anomaly_df = pd.read_csv(ANOMALY_FILE)

    anomaly_subset = anomaly_df.head(len(prediction_df)).copy()

    prediction_df["Anomaly"] = anomaly_subset["Anomaly"].values

    agent = RecommendationAgent()

    prediction_df["Recommendation"] = prediction_df.apply(
        lambda row: agent.generate_recommendation(
            row["Predicted"],
            row["Anomaly"]
        ),
        axis=1
    )

    print(prediction_df.head(10))

    prediction_df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("\nRecommendations saved to:")
    print(OUTPUT_FILE)