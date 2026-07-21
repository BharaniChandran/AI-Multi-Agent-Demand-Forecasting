from datetime import date

from pydantic import BaseModel


class SalesCreate(BaseModel):
    product_id: int
    quantity: int
    price: float
    sale_date: date


class SalesResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    price: float
    sale_date: date

    class Config:
        from_attributes = True