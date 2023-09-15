from sqlalchemy import update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

from database.orm.tables import session

from database.orm.tables import User, Items, Cart

# create
def add_user(user):
    
    session.add(user)

    session.commit()

# read
def get_users():

    #this method will return a list of users
    users = []

    results = session.query(User).all()

    for result in results:
        user = {f"First name": result.first_name, "Last name": result.last_name, "email": result.email, "items_list": result.items_list}

        users.append(user)

    session.commit()

    return users


# update 
def update_user(id, user):

    session.query(User).filter(User.id == id).update(
        {User.first_name: user.first_name, User.last_name: user.last_name, User.email: user.email, User.items_list: user.items_list}, synchronize_session=False)

    session.commit()

def delete_user(first_name, last_name):
    
    session.query(User).filter(User.first_name == first_name and User.last_name == last_name).delete()

    session.commit()


# cart

# create
def add_cart(cart):
    
    session.add(cart)

    session.commit()

# read
def get_cart():

    #this method will return a list of users
    carts = []

    results = session.query(Cart).all()

    for result in results:
        cart = {f"list of items": result.items_list}

        carts.append(cart)

    session.commit()

    return carts


# update 
def update_cart(id, cart):

    session.query(Cart).filter(Cart.id == id).update(
        {Cart.at1: cart.at1, Cart.items_list: cart.items_list}, synchronize_session=False)

    session.commit()

def delete_cart(id):
    
    session.query(Cart).filter(Cart.id == id).delete()

    session.commit()

#items
# create
def add_item(item):
    
    session.add(item)

    session.commit()

# read
def get_items():

    #this method will return a list of users
    items = []

    results = session.query(Items).all()

    for result in results:
        item = {f"name": result.name, "price": result.price, "quantity": result.quantity, "cart_id": result.cart_id}

        items.append(item)

    session.commit()

    return items


# update 
def update_item(id, item):

    session.query(Items).filter(Items.id == id).update(
        {Items.name: item.name, Items.price: item.price, Items.quantity: item.quantity}, synchronize_session=False)

    session.commit()

def delete_item(name):
    
    session.query(Items).filter(Items.name == name).delete()

    session.commit()
