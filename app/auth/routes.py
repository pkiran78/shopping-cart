from fastapi import APIRouter, Request, Depends, HTTPException, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from app.models import User
from app.database import es

templates = Jinja2Templates(directory="app/templates")

class User(BaseModel):
    username: str
    email: str
    password: str

auth_router = APIRouter()

@auth_router.get("/register")
async def get_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@auth_router.post("/register")
async def register(user: User):
    if es.exists(index="users", id=user.username):
        raise HTTPException(status_code=400, detail="User already exists")
    es.index(index="users", id=user.username, body=user.dict())
    return {"message": "User registered successfully"}

@auth_router.get("/list-users")
async def list_users(request: Request):
    users = es.search(index="users", body={"query": {"match_all": {}}})
    user_list = [user["_source"] for user in users["hits"]["hits"]]
    return templates.TemplateResponse("list_users.html", {"request": request, "users": user_list})

@auth_router.get("/login")
async def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@auth_router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    try:
        stored_user = es.get(index="users", id=username)["_source"]
        if stored_user["password"] != password:
            raise HTTPException(status_code=400, detail="Invalid credentials")
        return RedirectResponse(url="/shopping", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid credentials")
