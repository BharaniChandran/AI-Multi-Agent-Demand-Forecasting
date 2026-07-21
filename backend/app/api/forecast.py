from fastapi import APIRouter

router = APIRouter(prefix="/forecast", tags=["Forecast"])

@router.get("/")
def forecast():
    return {
        "status": "Forecast endpoint is working",
        "prediction": "Model not connected yet"
    }