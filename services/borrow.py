from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


from models.borrow import Borrows
from models.borrow import BorrowStatus
from models.user import User
from models.book import Book
from schemas.borrow import BorrowCreate, BorrowResponse
from schemas.response_custom import ResponseSchema


def increment_available_quantity(book_id: int, db: Session):
    try:
        book = db.query(Book).filter(Book.id == book_id).first()
        book.available_quantity += 1
        db.commit()
        db.refresh(book)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e._message())}",
        )
    return ResponseSchema(
        status="success",
        message="Available quantity incremented successfully",
        data=book,
    )


def decrement_available_quantity(book_id: int, db: Session):
    try:
        book = db.query(Book).filter(Book.id == book_id).first()
        book.available_quantity -= 1
        db.commit()
        db.refresh(book)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e._message())}",
        )
    return ResponseSchema(
        status="success",
        message="Available quantity decremented successfully",
        data=book,
    )


def create_borrow(borrow: BorrowCreate, user: User, db: Session) -> ResponseSchema:
    try:
        existing_borrow = (
            db.query(Borrows)
            .filter(
                Borrows.user_id == user.id,
                Borrows.book_id == borrow.book_id,
                Borrows.status != BorrowStatus.returned,
            )
            .first()
        )

        if existing_borrow:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You have already borrowed this book and not returned it yet.",
            )

        decrement_available_quantity(borrow.book_id, db)

        new_borrow = Borrows(**borrow.model_dump())
        new_borrow.user_id = user.id
        db.add(new_borrow)
        db.commit()
        db.refresh(new_borrow)

        response = BorrowResponse(
            book=new_borrow.book.title,
            borrow_date=new_borrow.borrow_date,
            due_date=new_borrow.due_date,
            borrower=new_borrow.user.name,
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
