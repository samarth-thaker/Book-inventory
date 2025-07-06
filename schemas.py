from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    stock: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    stock: int

class BookOut(BookBase):
    id: int
    class Config:
        orm_mode = True
