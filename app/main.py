from fastapi import FastAPI
from app.auth.routes import auth_router
from app.shopping.routes import shopping_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth")
app.include_router(shopping_router, prefix="/shopping")