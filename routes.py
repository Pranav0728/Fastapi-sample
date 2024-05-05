from fastapi import APIRouter, HTTPException, status
from models import Item
from database import db
from schema import list_serial
from bson import ObjectId

router = APIRouter()

@router.post("/items")
async def create_item(item: Item):
    new_item = await db.items.insert_one(item.dict())

@router.get("/items")
async def get_items():
    items = list_serial(db.items.find())
    return items

@router.put("/items/{id}")
async def put_items(id: str, item: Item):
    db.items.find_one_and_update({"_id": ObjectId(id)},{"$set":item.dict()}
    )

@router.delete("/items/{id}")
async def delete_item(id: str):
    db.items.find_one_and_delete({"_id":ObjectId(id)})

