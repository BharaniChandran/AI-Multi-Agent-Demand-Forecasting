import pandas as pd
from pathlib import Path
from sklearn.ensemble import IsolationForest

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "features.csv"


class AnomalyAgent:

    def __init__(self):

        self.model = IsolationForest(
            contamination=0.05,
            random_state=42
        )

    def detect(self, dataframe):

        features = dataframe[["Sales"]]

        dataframe = dataframe.copy()

        dataframe["Anomaly"] = self.model.fit_predict(features)

        return dataframe


if __name__ == "__main__":

    df = pd.read_csv(DATA_PATH)

    agent = AnomalyAgent()

    results = agent.detect(df)

    anomalies = results[results["Anomaly"] == -1]

    print("Detected Anomalies:\n")
    print(anomalies)

    OUTPUT = BASE_DIR / "data" / "processed" / "anomaly_results.csv"

    results.to_csv(OUTPUT, index=False)

    print("\nResults saved to:", OUTPUT)