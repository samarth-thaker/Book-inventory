from fastapi import HTTPException
from models import Book
#from schemas import BookCreate
#from . import models
#from sqlalchemy.orm import Session
def get_books(db):
    return db.query(Book).all
def get_books_by_id(db, id):
    return db.query(Book).filter(Book.id == id).first()
def create_book(db):
    new_book = Book(**Book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
def delete_book(db, id):
    book = db.quer(Book).filter(Book.id==id).first()
    if not book:
        raise HTTPException(status_code = 404, detail = 'Book not found')
    db.delete(book)
    db.commit()
    return {"message":"Book deleted successfully"}
def update_stock(db, id, newStock):
     book = db.query(Book).filter(Book.id==id).first()
     book.stock = book.stock + newStock
     db.commit()
     db.refresh(book)
     return {"message":"Book stock updated", "newStock":book.stock}