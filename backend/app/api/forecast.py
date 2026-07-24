from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from datetime import date, timedelta
import pandas as pd
import io

from app.services.forecast_service import ForecastService


router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"]
)


# Create one ForecastService instance.
forecast_service = ForecastService()


# ============================================================
# SINGLE / DATE-RANGE FORECAST REQUEST
# ============================================================

class ForecastRequest(BaseModel):
    store_id: int
    product_id: int
    price: float
    start_date: date
    end_date: date
    product_name: str
    category: str


# ============================================================
# DATE-RANGE FORECAST
# POST /forecast/
# ============================================================

@router.post("/")
def generate_forecast(request: ForecastRequest):
    """
    Generate product demand forecasts for a date range,
    detect anomalies, and generate inventory recommendation.
    """

    try:

        if request.start_date > request.end_date:
            raise HTTPException(
                status_code=400,
                detail="start_date must be before or equal to end_date"
            )

        forecast_results = []

        current_date = request.start_date
        final_result = None

        while current_date <= request.end_date:

            result = forecast_service.generate_forecast(
                store_id=request.store_id,
                product_id=request.product_id,
                price=request.price,
                date=str(current_date),
                product_name=request.product_name,
                category=request.category,
            )

            predicted_sales = result["prediction"]["predicted_sales"]

            forecast_results.append({
                "date": str(current_date),
                "sales": predicted_sales
            })

            final_result = result

            current_date += timedelta(days=1)

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


# ============================================================
# BULK CSV / EXCEL UPLOAD FORECAST
# POST /forecast/upload
# ============================================================

@router.post("/upload")
async def upload_forecast_file(
    file: UploadFile = File(...)
):
    """
    Upload CSV or Excel file and generate predictions
    for every row.
    """

    try:

        # ----------------------------------------------------
        # 1. Validate file type
        # ----------------------------------------------------

        if not file.filename:
            raise HTTPException(
                status_code=400,
                detail="No file was uploaded"
            )

        filename = file.filename.lower()

        if not (
            filename.endswith(".csv")
            or filename.endswith(".xlsx")
        ):
            raise HTTPException(
                status_code=400,
                detail="Only CSV (.csv) and Excel (.xlsx) files are supported"
            )


        # ----------------------------------------------------
        # 2. Read uploaded file
        # ----------------------------------------------------

        file_content = await file.read()

        if filename.endswith(".csv"):

            df = pd.read_csv(
                io.BytesIO(file_content)
            )

        else:

            df = pd.read_excel(
                io.BytesIO(file_content)
            )


        # ----------------------------------------------------
        # 3. Validate required columns
        # ----------------------------------------------------

        required_columns = [
            "store_id",
            "product_id",
            "price",
            "date",
            "product_name",
            "category"
        ]

        missing_columns = [
            column
            for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:
            raise HTTPException(
                status_code=400,
                detail={
                    "message": "Missing required columns",
                    "missing_columns": missing_columns,
                    "required_columns": required_columns
                }
            )


        # ----------------------------------------------------
        # 4. Generate predictions
        # ----------------------------------------------------

        predictions = []

        for _, row in df.iterrows():

            result = forecast_service.generate_forecast(
                store_id=int(row["store_id"]),
                product_id=int(row["product_id"]),
                price=float(row["price"]),
                date=str(row["date"]),
                product_name=str(row["product_name"]),
                category=str(row["category"]),
            )

            predicted_sales = result["prediction"]["predicted_sales"]

            predictions.append({
                "store_id": int(row["store_id"]),
                "product_id": int(row["product_id"]),
                "product_name": str(row["product_name"]),
                "category": str(row["category"]),
                "date": str(row["date"]),
                "price": float(row["price"]),
                "predicted_sales": predicted_sales
            })


        # ----------------------------------------------------
        # 5. Return predictions
        # ----------------------------------------------------

        return {
            "rows_processed": len(predictions),
            "predictions": predictions
        }


    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Bulk forecast generation failed: {str(e)}"
        )