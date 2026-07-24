from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.product import router as product_router
from app.api.sales import router as sales_router
from app.api.forecast import router as forecast_router


app = FastAPI(
    title="AI Multi-Agent Product Demand Forecasting System",
    description="Backend API for product management, sales data, and AI-powered demand forecasting.",
    version="1.0.0",
)


# CORS configuration for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5179",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register API routers
app.include_router(product_router)
app.include_router(sales_router)
app.include_router(forecast_router)


@app.get("/")
def root():
    return {
        "message": "AI Multi-Agent Product Demand Forecasting System API is running",
        "status": "success",
        "docs": "/docs",
        "forecast_endpoint": "/forecast/",
    }