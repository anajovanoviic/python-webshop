from sqlalchemy import Column, String, Integer, CHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import postgresql

from sqlalchemy.engine import URL

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column("id", Integer, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    email = Column("email", String)
    items_list = Column("items", postgresql.ARRAY(String))

    def __init__(self, id, first_name, last_name, email, items_list):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.items_list = items_list

class Items(Base):
    __tablename__ = "items"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    price = Column("price", Integer) # maybe float?
    quantity = Column("quantity", Integer)
    cart_id = Column(Integer, ForeignKey("cart.id"))

    def __init__(self, id, name, price, quantity, cart_id):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.cart_id = cart_id
    
    def __repr__(self):
        return f"({self.id}) {self.name} is inside {self.cart_id}"

class Cart(Base):
    __tablename__ = "cart"
    id = Column("id", Integer, primary_key=True)
    at1 = Column("at1", String)
    items_list = Column("items", postgresql.ARRAY(String))

    def __init__(self, id, at1, items_list):
        self.id = id
        self.at1 = at1
        self.items_list = items_list

    def __repr__(self):
        return f"({self.id}) {self.at1}"

url = URL.create(
    drivername="postgresql",
    username="ana",
    password="francuski1",
    #host="192.168.1.102",
    host="10.113.80.15",
    database="ana"
)

engine = create_engine(url)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
""" 
user = User(1, "Ana", "Jovanovic", "ana@gmail.com", ["fish", "eggs", "water"])
session.add(user)
session.commit()

cart1 = Cart(1, "primer", ["hleb", "jaja", "voce"])
session.add(cart1)
session.commit()

item = Items(1, "hleb", 2, 3, cart1.id)
session.add(item)
session.commit()

results = session.query(Items, Cart).filter(Items.cart_id == Cart.id).filter(Cart.at1 == "primer").all()
for r in results:
    print(r) """

