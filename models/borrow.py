from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date
from config.database import Base


class Borrows(Base):
    __tablename__ = "borrows"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(
        Integer,
        ForeignKey(
            "books.id",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    user_id = Column(
        Integer,
        ForeignKey(
            "users.id",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    borrow_date = Column(Date, nullable=False, default=date.today)
    due_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)

    books = relationship("Book", back_populates="borrows")
    users = relationship("User", back_populates="borrows")
