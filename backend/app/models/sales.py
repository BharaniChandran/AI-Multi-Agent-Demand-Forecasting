from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.models.product import Base


class Sales(Base):
    __tablename__ = "sales"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    quantity = Column(
        Integer,
        nullable=False
    )

    price = Column(
        Float,
        nullable=False
    )

    sale_date = Column(
        Date,
        nullable=False
    )

    product = relationship(
        "Product",
        backref="sales"
    )