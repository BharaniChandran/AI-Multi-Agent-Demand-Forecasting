from app.database.database import engine
from app.models.product import Base

Base.metadata.create_all(bind=engine)

print("Database Created Successfully!")