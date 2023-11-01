from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

inventory = {
}

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None #you can also set it as a default value




@app.get("/")
def home():
    return {"Data:": "Testing"}

@app.get("/about")
def about():
    return {"Data": "About"}

@app.get("/get-item/{item_id}")
def get_item(item_id: int): #description is showed in /docs
    return inventory[item_id]

@app.get("/get-item-mp/{item_id}/{name}") #where mp = multiple parameters
def get_item_mp(*, item_id: int, name: Optional[str] = None): #Optional[str] = None means not required param
    return inventory[item_id] #idk how to use yet

#query parameters
@app.get("/get-by-name") #/get-by-name?name=<name>
def get_by_name(name: str):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
        
    return {"Data": "Not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item already exists"}
    inventory[item_id] = item
    return inventory[item_id]

#progress 35mins at request body and POST methods