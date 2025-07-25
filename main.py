from fastapi import Depends, FastAPI, HTTPException

from models.user import User
from config.database import Base, engine
from core.exception_handlers import http_exception_handler
from core.oauth2 import get_current_user

from routes import auth, category, book, borrow

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.add_exception_handler(HTTPException, http_exception_handler)

app.include_router(auth.router, prefix="/api")
app.include_router(category.router, prefix="/api")
app.include_router(book.router, prefix="/api")
app.include_router(borrow.router, prefix="/api")

@app.get("/")
def root(current_user: User = Depends(get_current_user)):
    return {"message": "Library Management!"}
