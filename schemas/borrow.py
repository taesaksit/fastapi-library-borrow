from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from models.borrow import BorrowStatus


class BorrowBase(BaseModel):
    book_id: int
    user_id: Optional[int] = None
    borrow_date: Optional[date] = Field(default_factory=date.today)
    due_date: date = None
    return_date: Optional[date] = None
    status: Optional[BorrowStatus] = BorrowStatus.borrowed


class BorrowCreate(BorrowBase):
    pass

# Custom
class BorrowResponse(BaseModel):
    borrower: str
    book: str
    borrow_date: date
    due_date: date

# Default
# class BorrowResponse(BorrowBase):
#     pass
#     class Config:
#         from_attributes = True