from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import date, timedelta

from app.services.forecast_service import ForecastService


router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"]
)


# Create one ForecastService instance.
# The ML agents and trained model will be initialized once.
forecast_service = ForecastService()


class ForecastRequest(BaseModel):
    store_id: int
    product_id: int
    price: float
    start_date: date
    end_date: date
    product_name: str
    category: str


@router.post("/")
def generate_forecast(request: ForecastRequest):
    """
    Generate product demand forecasts for a date range,
    detect anomalies,
    and generate inventory recommendation.
    """

    try:

        # Validate date range
        if request.start_date > request.end_date:
            raise HTTPException(
                status_code=400,
                detail="start_date must be before or equal to end_date"
            )

        forecast_results = []

        # Start from the requested start date
        current_date = request.start_date

        # Generate prediction for every date in the range
        while current_date <= request.end_date:

            result = forecast_service.generate_forecast(
                store_id=request.store_id,
                product_id=request.product_id,
                price=request.price,
                date=str(current_date),
                product_name=request.product_name,
                category=request.category,
            )

            # Extract predicted sales from the existing ML response
            predicted_sales = result["prediction"]["predicted_sales"]

            # Add date and prediction to forecast list
            forecast_results.append({
                "date": str(current_date),
                "sales": predicted_sales
            })

            # Move to next date
            current_date += timedelta(days=1)

        # Use the anomaly and recommendation from the final prediction
        final_result = result

        return {
            "forecast": forecast_results,
            "anomaly": final_result.get(
                "anomaly",
                {
                    "status": "Normal"
                }
            ),
            "recommendation": final_result.get(
                "recommendation",
                {
                    "message": "No recommendation available"
                }
            )
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Forecast generation failed: {str(e)}"
        )