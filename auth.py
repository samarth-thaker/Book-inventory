from fastapi import APIRouter, Depends, HTTPException,Form
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = 'token')
auth_router  =  APIRouter()
@auth_router.post("/token")
def login(username : str = Form(...), password:str = Form(...)):
    print("Login attempt: ", username, password)
    return {"access_token" : "admin-token", "token-type":"bearer"}
def is_admin(token: str = Depends(oauth2_scheme)):
    if token!="admin token":
        raise HTTPException(status_code = 403, detail="Not authorized as admin")