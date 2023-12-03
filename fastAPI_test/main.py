from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

inventory = {
}

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None #you can also set it as a default value
    #access class items using .n

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
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

@app.post("/create-item/{item_id}") #hardcode access in /docs
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item already exists"}
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item does not exist"}
    
    #hard coded because the guy example sucks lol
    inventory[item_id].name = item.name
    inventory[item_id].price = item.price
    inventory[item_id].brand = item.brand
    return inventory[item_id]


@app.delete("/delete-item") #e.g. request URL http://127.0.0.1:8000/delete-item?item_id=1
def delete_item(item_id: int = Query(..., description="The ID of the item to delete")):
    if item_id not in inventory:
        return {"Error": "Item not found"}
    
    del inventory[item_id]
    return {"Success": "Item has been deleted!"}


#status codes

@app.get("/custom-status")
def custom_status():
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="any Error message for you to input")
    #raise HTTPException(status_code=status.) shows all the status codes ; status.
#testing

# @app.get("/get-all-items")
# def get_all_items():
#     #for now just gets the name of all the items and adds it in a string
#     all_items = ""
#     for item_id in inventory:
#         all_items = all_items + "{}: {}\n".format(inventory[item_id].name + str(inventory[item_id].price))
#         #print(item_id)
#     return {"test": len(inventory)}
#     #return {"All items": all_items}