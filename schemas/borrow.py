from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from schemas.book import BookResponse
from schemas.user import UserResponse


class BorrowBase(BaseModel):
    book_id: int
    user_id: Optional[int] = None
    borrow_date: Optional[date] = Field(default_factory=date.today)
    due_date: date = None
    return_date: Optional[date] = None


class BorrowCreate(BorrowBase):
    pass


class BorrowResponse(BaseModel):
    book: str
    borrow_date: date
    due_date: date
