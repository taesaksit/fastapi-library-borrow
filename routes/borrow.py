from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from config.database import get_db
from schemas.response_custom import ResponseSchema
from schemas.borrow import BorrowCreate, BorrowResponse
from services import borrow as services
from models.user import User
from core.oauth2 import get_current_user

router = APIRouter(prefix="/borrow")


@router.post("/", response_model=ResponseSchema[BorrowResponse], tags=["borrow"])
def create_borrow(
    borrow: BorrowCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return services.create_borrow(borrow, db)
