from fastapi import FastAPI

# Import API routers
from app.api.forecast import router as forecast_router
from app.api.product import router as product_router

# Create FastAPI application
app = FastAPI(
    title="AI Multi-Agent Demand Forecasting API",
    version="1.0.0",
    description="Backend API for Product Management and Demand Forecasting"
)

# Register routers
app.include_router(forecast_router)
app.include_router(product_router)

# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Backend API is running successfully!"
    }