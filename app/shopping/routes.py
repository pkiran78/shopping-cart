from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from app.models import Item
from app.database import es
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

templates = Jinja2Templates(directory="app/templates")
shopping_router = APIRouter()

@shopping_router.get("/")
async def get_shopping(request: Request):
    items = es.search(index="items", body={"query": {"match_all": {}}})
    item_list = [item["_source"] for item in items["hits"]["hits"]]
    return templates.TemplateResponse("shopping.html", {"request": request, "items": item_list})

@shopping_router.post("/add-item")
async def add_item(name: str = Form(...), description: str = Form(...), price: float = Form(...)):
    item = Item(name=name, description=description, price=price)
    es.index(index="items", body=item.dict())
    logger.info(f"Item {name} added successfully")
    return {"message": "Item added successfully"}

@shopping_router.get("/items")
async def get_items():
    items = es.search(index="items", body={"query": {"match_all": {}}})
    return items["hits"]["hits"]
