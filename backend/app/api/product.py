from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.product import Product
from app.schemas.product_schema import ProductCreate, ProductResponse


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


# ---------------------------------------------------------
# CREATE PRODUCT
# POST /products/
# ---------------------------------------------------------
@router.post("/", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    new_product = Product(
        name=product.name,
        category=product.category
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


# ---------------------------------------------------------
# GET ALL PRODUCTS
# GET /products/
# ---------------------------------------------------------
@router.get("/", response_model=list[ProductResponse])
def get_products(
    db: Session = Depends(get_db)
):

    products = db.query(Product).all()

    return products


# ---------------------------------------------------------
# GET PRODUCT BY ID
# GET /products/{product_id}
# ---------------------------------------------------------
@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return product


# ---------------------------------------------------------
# UPDATE PRODUCT
# PUT /products/{product_id}
# ---------------------------------------------------------
@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    updated_product: ProductCreate,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product.name = updated_product.name
    product.category = updated_product.category

    db.commit()
    db.refresh(product)

    return product


# ---------------------------------------------------------
# DELETE PRODUCT
# DELETE /products/{product_id}
# ---------------------------------------------------------
@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    db.delete(product)
    db.commit()

    return {
        "message": "Product deleted successfully"
    }