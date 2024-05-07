from pydantic import BaseModel

class Item(BaseModel):
    todo: str

    class Config:
         from_attributes = True