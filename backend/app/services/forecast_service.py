import pandas as pd

from ml.agents.forecasting_agent import ForecastingAgent
from ml.agents.anomaly_agent import AnomalyAgent
from ml.agents.recommendation_agent import RecommendationAgent

from app.services.ml_preprocessing import prepare_forecast_input


class ForecastService:
    """
    Service responsible for connecting the Backend
    with the ML forecasting, anomaly detection,
    and recommendation agents.
    """

    def __init__(self):
        """
        Initialize all ML agents once when the service starts.
        """

        self.forecasting_agent = ForecastingAgent()
        self.anomaly_agent = AnomalyAgent()
        self.recommendation_agent = RecommendationAgent()

    def generate_forecast(
        self,
        store_id: int,
        product_id: int,
        price: float,
        date: str,
        product_name: str,
        category: str,
    ):
        """
        Generate a complete demand forecasting result.

        Workflow:

        1. Prepare input data
        2. Generate sales prediction
        3. Detect anomaly
        4. Generate inventory recommendation
        5. Return unified response
        """

        # ---------------------------------------------------------
        # STEP 1: Prepare input data
        # ---------------------------------------------------------

        input_dataframe = prepare_forecast_input(
            store_id=store_id,
            product_id=product_id,
            price=price,
            date=date,
            product_name=product_name,
            category=category,
        )

        # ---------------------------------------------------------
        # STEP 2: Generate sales prediction
        # ---------------------------------------------------------

        prediction = self.forecasting_agent.forecast(
            input_dataframe
        )

        # Convert NumPy prediction to normal Python float.
        predicted_sales = float(prediction[0])

        # ---------------------------------------------------------
        # STEP 3: Prepare data for anomaly detection
        # ---------------------------------------------------------

        anomaly_dataframe = pd.DataFrame(
            {
                "Sales": [predicted_sales]
            }
        )

        # ---------------------------------------------------------
        # STEP 4: Detect anomaly
        # ---------------------------------------------------------

        anomaly_result = self.anomaly_agent.detect(
            anomaly_dataframe
        )

        # Get anomaly value from the result.
        anomaly = int(
            anomaly_result.iloc[0]["Anomaly"]
        )

        # Convert anomaly value into readable status.
        if anomaly == -1:
            anomaly_status = "Anomaly Detected"
        else:
            anomaly_status = "Normal"

        # ---------------------------------------------------------
        # STEP 5: Generate recommendation
        # ---------------------------------------------------------

        recommendation = (
            self.recommendation_agent.generate_recommendation(
                predicted_sales,
                anomaly
            )
        )

        # ---------------------------------------------------------
        # STEP 6: Return unified response
        # ---------------------------------------------------------

        return {
            "prediction": {
                "predicted_sales": predicted_sales
            },
            "anomaly": {
                "status": anomaly_status,
                "value": anomaly
            },
            "recommendation": {
                "message": recommendation
            }
        }