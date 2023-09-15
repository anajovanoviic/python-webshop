from fastapi import FastAPI
from database.orm import db_connect as db

from database.orm.Users import User
from database.orm.Items import Items


app = FastAPI()

@app.get("/")
def home_page():
    return "Welcome to online shop :)"

# what is async Lec 9 45:00, but not completely clear to me 

# create
@app.post("/add_user")
async def add_user(id: int, first_name: str, last_name: str, email: str):
    user = User(id, first_name, last_name, email)
    db.add_user(user)

# read
@app.get("/users")
async def get_users():
    return db.get_users()

# update
@app.post("/update_user")
async def update_user(id: int, first_name: str, last_name: str, email: str):
    user = User(id, first_name, last_name, email)
    return db.update_user(id, user)

# delete
@app.post("/delete_user")
async def delete_user(first_name: str, last_name: str):
    db.delete_user(first_name, last_name)


@app.post("/add_item_to_the_offer")
async def add_item(id: int, name: str, price: float, quantity:float):
    item = Items
    db.add_item()