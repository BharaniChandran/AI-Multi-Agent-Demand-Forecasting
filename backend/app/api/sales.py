import csv
import io
from datetime import date

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.product import Product
from app.models.sales import Sales
from app.schemas.sales_schema import SalesCreate, SalesResponse


# =========================================================
# CREATE SALES API ROUTER
# =========================================================

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

    # Add record to database
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

    # Check whether the updated product exists
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

    # Delete sales record
    db.delete(sales)
    db.commit()

    return {
        "message": "Sales record deleted successfully"
    }


# =========================================================
# UPLOAD SALES CSV
# POST /sales/upload
# =========================================================

@router.post("/upload")
async def upload_sales_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # -----------------------------------------------------
    # 1. CHECK FILE NAME
    # -----------------------------------------------------

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file was selected"
        )

    # Check CSV extension
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed"
        )

    # -----------------------------------------------------
    # 2. READ UPLOADED FILE
    # -----------------------------------------------------

    contents = await file.read()

    if not contents:
        raise HTTPException(
            status_code=400,
            detail="Uploaded CSV file is empty"
        )

    # -----------------------------------------------------
    # 3. DECODE CSV FILE
    # -----------------------------------------------------

    try:
        decoded_contents = contents.decode("utf-8-sig")

    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="CSV file must use UTF-8 encoding"
        )

    # -----------------------------------------------------
    # 4. CREATE CSV READER
    # -----------------------------------------------------

    csv_file = io.StringIO(decoded_contents)

    reader = csv.DictReader(csv_file)

    # -----------------------------------------------------
    # 5. CHECK CSV HEADERS
    # -----------------------------------------------------

    required_columns = {
        "product_id",
        "quantity",
        "price",
        "sale_date"
    }

    if not reader.fieldnames:
        raise HTTPException(
            status_code=400,
            detail="CSV file is empty or has no header"
        )

    # Remove extra spaces from column names
    actual_columns = {
        column.strip()
        for column in reader.fieldnames
        if column
    }

    missing_columns = required_columns - actual_columns

    if missing_columns:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "CSV is missing required columns",
                "required_columns": list(required_columns),
                "missing_columns": list(missing_columns)
            }
        )

    # -----------------------------------------------------
    # 6. PROCESS CSV ROWS
    # -----------------------------------------------------

    successful_records = 0
    failed_records = []

    for row_number, row in enumerate(reader, start=2):

        try:
            # ---------------------------------------------
            # Read values from CSV
            # ---------------------------------------------

            product_id_value = row.get("product_id")
            quantity_value = row.get("quantity")
            price_value = row.get("price")
            sale_date_value = row.get("sale_date")

            # ---------------------------------------------
            # Check empty values
            # ---------------------------------------------

            if not product_id_value:
                raise ValueError(
                    "product_id cannot be empty"
                )

            if not quantity_value:
                raise ValueError(
                    "quantity cannot be empty"
                )

            if not price_value:
                raise ValueError(
                    "price cannot be empty"
                )

            if not sale_date_value:
                raise ValueError(
                    "sale_date cannot be empty"
                )

            # ---------------------------------------------
            # Convert values to correct data types
            # ---------------------------------------------

            product_id = int(product_id_value)

            quantity = int(quantity_value)

            price = float(price_value)

            sale_date = date.fromisoformat(
                sale_date_value.strip()
            )

            # ---------------------------------------------
            # Validate product ID
            # ---------------------------------------------

            if product_id <= 0:
                raise ValueError(
                    "product_id must be greater than 0"
                )

            # ---------------------------------------------
            # Validate quantity
            # ---------------------------------------------

            if quantity <= 0:
                raise ValueError(
                    "quantity must be greater than 0"
                )

            # ---------------------------------------------
            # Validate price
            # ---------------------------------------------

            if price < 0:
                raise ValueError(
                    "price cannot be negative"
                )

            # ---------------------------------------------
            # Check product exists
            # ---------------------------------------------

            product = db.query(Product).filter(
                Product.id == product_id
            ).first()

            if product is None:
                raise ValueError(
                    f"Product with ID {product_id} does not exist"
                )

            # ---------------------------------------------
            # Create new sales record
            # ---------------------------------------------

            new_sales = Sales(
                product_id=product_id,
                quantity=quantity,
                price=price,
                sale_date=sale_date
            )

            db.add(new_sales)

            successful_records += 1

        except ValueError as error:

            # Add invalid row information
            failed_records.append({
                "row": row_number,
                "error": str(error)
            })

        except Exception as error:

            # Handle unexpected errors
            failed_records.append({
                "row": row_number,
                "error": str(error)
            })

    # -----------------------------------------------------
    # 7. COMMIT VALID RECORDS
    # -----------------------------------------------------

    try:
        db.commit()

    except Exception as error:
        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"Database error while saving sales data: {str(error)}"
        )

    # -----------------------------------------------------
    # 8. RETURN UPLOAD RESULT
    # -----------------------------------------------------

    return {
        "message": "Sales CSV processing completed",
        "filename": file.filename,
        "successful_records": successful_records,
        "failed_records": len(failed_records),
        "errors": failed_records
    }