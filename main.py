from fastapi import FastAPI
from routers.books import router
from database import create_db
from auth import auth_router
app = FastAPI(
    title="Book store inventory API",
    version="1.0.0",
    description="Manage books, stock updates, and admin using FastAPI + SQLite"
)


create_db()
app.include_router(auth_router)
app.include_router(router, prefix="/api/v1", tags=["Books"])
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
