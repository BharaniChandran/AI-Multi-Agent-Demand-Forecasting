from datetime import date

from pydantic import BaseModel, Field


class SalesCreate(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity: int = Field(..., gt=0)
    price: float = Field(..., ge=0)
    sale_date: date


class SalesResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    price: float
    sale_date: date

    class Config:
        from_attributes = True