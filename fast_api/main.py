from fastapi import FastAPI
from database.orm import db_ops as db

from database.orm.tables import User, Items, Cart

app = FastAPI()

@app.get("/")
def home_page():
    return "Welcome to online shop :)"

# create
@app.post("/add_user")
async def add_user(id: int, first_name: str, last_name: str, email: str, items_list: list[str]):
    user = User(id, first_name, last_name, email, items_list)
    db.add_user(user)

# read
@app.get("/users")
async def get_users():
    return db.get_users()

# update
@app.post("/update_user")
async def update_user(id: int, first_name: str, last_name: str, email: str, items_list: list[str]):
    user = User(id, first_name, last_name, email, items_list)
    return db.update_user(id, user)

# delete
@app.post("/delete_user")
async def delete_user(first_name: str, last_name: str):
    db.delete_user(first_name, last_name)

#cart
# create
@app.post("/add_cart")
async def add_cart(id: int, at1: str, items_list: list[str]):
    cart = Cart(id, at1, items_list)
    db.add_cart(cart)

# read
@app.get("/carts")
async def get_carts():
    return db.get_cart()

# update
@app.post("/update_cart")
async def update_cart(id: int, at1: str, items_list: list[str]):
    cart = Cart(id, at1, items_list)
    return db.update_cart(id, cart)

# delete
@app.post("/delete_cart")
async def delete_cart(id: str):
    db.delete_cart(id)

# items
# create
@app.post("/add_item")
async def add_item(id: int, name: str, price: int, quantity: str):
    item = Items(id, name, price, quantity)
    db.add_item(item)

# read
@app.get("/items")
async def get_items():
    return db.get_items()

# update
@app.post("/update_user")
async def update_user(id: int, first_name: str, last_name: str, email: str, items_list: list[str]):
    user = User(id, first_name, last_name, email, items_list)
    return db.update_user(id, user)

# delete
@app.post("/delete_user")
async def delete_user(first_name: str, last_name: str):
    db.delete_user(first_name, last_name)

    
