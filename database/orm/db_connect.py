from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

#from database.orm.Users import User
from Users import User
#from database.orm.Items import Items
from Items import Items
from Cart import Cart


url = URL.create(
    drivername="postgresql",
    username="ana",
    password="francuski1",
    host="192.168.1.102",
    database="ana"
)

def create_session():
    engine = create_engine(url)

    #Person.__table__.create(bind=engine, checkfirst=True)
    User.__table__.create(bind=engine, checkfirst=True)

    Session = sessionmaker(bind=engine)

    return Session()

# create
def add_user(user):
    session = create_session()

    session.add(user)

    session.commit()

#user = User(1, "Ana", "Jovanovic", "ana@gmail.com")
#add_user(user)

# read
def get_users():

    #this method will return a list of users
    users = []

    session = create_session()

    results = session.query(User).all()

    for result in results:
        user = {f"First name": result.first_name, "Last name": result.last_name, "email": result.email}

        users.append(user)

    session.commit()

    return users


# update 
def update_user(id, user):
    session = create_session()

    session.query(User).filter(User.id == id).update(
        {User.first_name: user.first_name, User.last_name: user.last_name, User.email: user.email}, synchronize_session=False
    )

    session.commit()


# delete
def delete_user(first_name, last_name):
    session = create_session()

    session.query(User).filter(User.first_name == first_name and User.last_name == last_name).delete()

    session.commit()
 
def create_item_session():
    engine = create_engine(url)

    #Person.__table__.create(bind=engine, checkfirst=True)
    Items.__table__.create(bind=engine, checkfirst=True)

    Session = sessionmaker(bind=engine)

    return Session()

def add_item(item):
    session = create_item_session()

    session.add(item)

    session.commit() 



#item = Items(1, "hleb", 2, 3)
#add_item(item)

def create_cart_session():
    engine = create_engine(url)

    #Person.__table__.create(bind=engine, checkfirst=True)
    Cart.__table__.create(bind=engine, checkfirst=True)

    Session = sessionmaker(bind=engine)

    return Session()

def add_cart(cart):
    session = create_cart_session()

    session.add(cart)

    session.commit()

    
cart1 = Cart(1, "primer")
add_cart(cart1) #ovo radi

item = Items(1, "hleb", 2, 3, cart1.id)
add_item(item)
