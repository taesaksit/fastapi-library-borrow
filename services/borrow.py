from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


from models.borrow import Borrows
from models.book import Book
from schemas.borrow import BorrowCreate, BorrowResponse
from schemas.response_custom import ResponseSchema


def create_borrow(borrow: BorrowCreate, db: Session) -> ResponseSchema:
    try:
        new_borrow = Borrows(**borrow.model_dump())
        db.add(new_borrow)
        db.commit()
        db.refresh(new_borrow)

        response = BorrowResponse(
            book=new_borrow.books.title,
            borrow_date=new_borrow.borrow_date,
            due_date=new_borrow.due_date,
        )
        
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e._message())}",
        )

    return ResponseSchema(
        status="success",
        message="Borrow created successfully",
        data=response,
    )
