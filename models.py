from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price:float

    class Config:
         from_attributes = True