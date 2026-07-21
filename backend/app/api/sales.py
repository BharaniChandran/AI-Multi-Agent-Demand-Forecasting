from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.product import Product
from app.models.sales import Sales
from app.schemas.sales_schema import SalesCreate, SalesResponse


# Create Sales API router
router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)


# =========================================================
# CREATE SALES RECORD
# POST /sales/
# =========================================================
@router.post("/", response_model=SalesResponse)
def create_sales(
    sales: SalesCreate,
    db: Session = Depends(get_db)
):
    # Check whether the product exists
    product = db.query(Product).filter(
        Product.id == sales.product_id
    ).first()

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    # Create new sales record
    new_sales = Sales(
        product_id=sales.product_id,
        quantity=sales.quantity,
        price=sales.price,
        sale_date=sales.sale_date
    )

    # Save to database
    db.add(new_sales)
    db.commit()
    db.refresh(new_sales)

    return new_sales


# =========================================================
# GET ALL SALES RECORDS
# GET /sales/
# =========================================================
@router.get("/", response_model=list[SalesResponse])
def get_sales(
    db: Session = Depends(get_db)
):
    sales_records = db.query(Sales).all()

    return sales_records


# =========================================================
# GET SALES RECORD BY ID
# GET /sales/{sales_id}
# =========================================================
@router.get("/{sales_id}", response_model=SalesResponse)
def get_sales_by_id(
    sales_id: int,
    db: Session = Depends(get_db)
):
    sales = db.query(Sales).filter(
        Sales.id == sales_id
    ).first()

    if sales is None:
        raise HTTPException(
            status_code=404,
            detail="Sales record not found"
        )

    return sales


# =========================================================
# UPDATE SALES RECORD
# PUT /sales/{sales_id}
# =========================================================
@router.put("/{sales_id}", response_model=SalesResponse)
def update_sales(
    sales_id: int,
    updated_sales: SalesCreate,
    db: Session = Depends(get_db)
):
    # Find existing sales record
    sales = db.query(Sales).filter(
        Sales.id == sales_id
    ).first()

    if sales is None:
        raise HTTPException(
            status_code=404,
            detail="Sales record not found"
        )

    # Check whether the new product exists
    product = db.query(Product).filter(
        Product.id == updated_sales.product_id
    ).first()

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    # Update sales record
    sales.product_id = updated_sales.product_id
    sales.quantity = updated_sales.quantity
    sales.price = updated_sales.price
    sales.sale_date = updated_sales.sale_date

    # Save changes
    db.commit()
    db.refresh(sales)

    return sales


# =========================================================
# DELETE SALES RECORD
# DELETE /sales/{sales_id}
# =========================================================
@router.delete("/{sales_id}")
def delete_sales(
    sales_id: int,
    db: Session = Depends(get_db)
):
    # Find sales record
    sales = db.query(Sales).filter(
        Sales.id == sales_id
    ).first()

    if sales is None:
        raise HTTPException(
            status_code=404,
            detail="Sales record not found"
        )

    # Delete record
    db.delete(sales)
    db.commit()

    return {
        "message": "Sales record deleted successfully"
    }