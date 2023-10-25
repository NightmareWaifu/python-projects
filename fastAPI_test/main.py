from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

inventory = {
    1: {
        "name": "Milk",
        "price": 3.99,
        "brand": "Regular"
            }
}

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
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
        
    return {"Data": "Not found"}


#progress 35mins at request body and POST methods