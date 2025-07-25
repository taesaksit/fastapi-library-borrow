from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from config.database import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(
        Integer,
        ForeignKey(
            "categories.id",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
    )
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    available_quantity = Column(Integer, nullable=False)

    category = relationship("Category", back_populates="books")
    borrows = relationship("Borrows", back_populates="books")