from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import date

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
    date: date
    product_name: str
    category: str


@router.post("/")
def generate_forecast(request: ForecastRequest):
    """
    Generate product demand forecast,
    detect anomalies,
    and generate inventory recommendation.
    """

    try:

        result = forecast_service.generate_forecast(
            store_id=request.store_id,
            product_id=request.product_id,
            price=request.price,
            date=str(request.date),
            product_name=request.product_name,
            category=request.category,
        )

        return result

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Forecast generation failed: {str(e)}"
        )