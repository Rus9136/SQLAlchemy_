from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models


app = FastAPI()

db = SessionLocal()

class Item(BaseModel): #serializer
    id: int
    user_id: int
    category: str
    amount: int
    description: str

    class Config:
        orm_mode=True

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/items', response_model=Item,
          status_code=status.HTTP_201_CREATED)
def create_an_item(item: Item):
    db_item = db.query(models.Operation).filter(models.Operation.id == item.id).first()

    if db_item is not None:
        raise HTTPException(status_code=400, detail="Item already exists")

    new_item = models.Operation(
        user_id=item.user_id,
        category=item.category,
        description=item.description,
        amount=item.amount,
        date='2022-03-19'
    )

    db.add(new_item)
    db.commit()

    return new_item