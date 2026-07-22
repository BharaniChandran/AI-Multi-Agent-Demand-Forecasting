from fastapi import FastAPI

from app.api.product import router as product_router
from app.api.sales import router as sales_router
from app.api.forecast import router as forecast_router


# Create the FastAPI application.
app = FastAPI(
    title="AI Multi-Agent Product Demand Forecasting System",
    description=(
        "Backend API for product management, sales management, "
        "CSV sales upload, demand forecasting, anomaly detection, "
        "and inventory recommendations."
    ),
    version="1.0.0",
)


# ---------------------------------------------------------
# Product APIs
# ---------------------------------------------------------
# Existing Product CRUD endpoints remain unchanged.
#
# Examples:
# POST   /products/
# GET    /products/
# GET    /products/{product_id}
# PUT    /products/{product_id}
# DELETE /products/{product_id}
# ---------------------------------------------------------

app.include_router(product_router)


# ---------------------------------------------------------
# Sales APIs
# ---------------------------------------------------------
# Existing Sales CRUD and CSV upload endpoints remain unchanged.
#
# Examples:
# POST /sales/
# GET  /sales/
# POST /sales/upload
# ---------------------------------------------------------

app.include_router(sales_router)


# ---------------------------------------------------------
# Forecast APIs
# ---------------------------------------------------------
# New ML integration endpoint.
#
# Current endpoint:
# POST /forecast/
#
# This connects:
# FastAPI
#     ↓
# Forecast Router
#     ↓
# Forecast Service
#     ↓
# ML Preprocessing
#     ↓
# Forecasting Agent
#     ↓
# Random Forest Model
#     ↓
# Recommendation Agent
# ---------------------------------------------------------

app.include_router(forecast_router)


# ---------------------------------------------------------
# Root Endpoint
# ---------------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "AI Multi-Agent Product Demand Forecasting System API",
        "status": "running",
        "version": "1.0.0",
        "services": {
            "products": "available",
            "sales": "available",
            "forecast": "available",
        },
    }