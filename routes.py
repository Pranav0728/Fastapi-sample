from fastapi import APIRouter, HTTPException, status
from models import Item
from database import db
from schema import list_serial
from bson import ObjectId

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    db.items.insert_one(item.dict())

@router.get("/")
async def get_items():
    items = list_serial(db.items.find())
    return items

@router.put("/{id}", response_model=Item)
async def update_item(id: str, item: Item):
    db.items.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": item.dict()},
        return_document=True
    )


@router.delete('/{id}')
async def delete_item(id: str):
     db.items.find_one_and_delete({"_id": ObjectId(id)})
