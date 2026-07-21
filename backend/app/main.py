from fastapi import FastAPI

from app.api.forecast import router as forecast_router
from app.api.product import router as product_router
from app.api.sales import router as sales_router


app = FastAPI(
    title="AI Multi-Agent Demand Forecasting API",
    version="1.0.0",
    description="Backend API for Product Management and Demand Forecasting"
)


app.include_router(forecast_router)
app.include_router(product_router)
app.include_router(sales_router)


@app.get("/")
def home():
    return {
        "message": "Backend API is running successfully!"
    }