from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str


class Item(BaseModel):
    name: str
    description: str
    price: float
