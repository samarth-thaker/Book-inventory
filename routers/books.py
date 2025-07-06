from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth import is_admin
from database import SessionLocal
import crud
import schemas

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/books")
def list_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@router.get("/books", response_model= schemas.BookOut, status_code=201)
def create_book(book: schemas.BookCreate, db:Session=Depends(get_db), _=Depends(is_admin)):
    return crud.create_book(db, book)
@router.put("/books/{id}/stock", response_model= schemas.BookOut, status_code=201)
def update_book_stock(id:int, book: schemas.BookCreate, db:Session=Depends(get_db), _=Depends(is_admin)):
    return crud.create_book(db, id, book.stock)
@router.delete("books/{id}", status_code=204)
def delete_book(id: int, db:Session = Depends(get_db), _=Depends(is_admin)):
    crud.delete_book(id, db)
    return{"Detail": "Book deleted"}