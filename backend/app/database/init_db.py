from app.database.database import engine
from app.models.product import Base
from app.models.product import Product
from app.models.sales import Sales


# Create all database tables
Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")