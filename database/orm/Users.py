from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import ARRAY

#from final_task.Items import Items
#from database.orm.Items import Items


Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column("id", Integer, primary_key=True)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String)
    email = Column("email", String)
    #items_list = Column(ARR)
    #items = relationship("Items")
    items_list = Column("items", ARRAY(Integer))

    #items = Column("items", Items) #strani kljuc
    #items_list = relationship('Items', backref='user')

    # ovo dole uncomment and add later
    #items_list = Column(Integer, ForeignKey("items.id"))

    def __init__(self, id, first_name, last_name, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        #self.items_list = items_list

""" from sqlalchemy import Column, String, Integer, CHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Items(Base):
    __tablename__ = "items"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    price = Column("price", Integer) # maybe float?
    quantity = Column("quantity", Integer)
    

    #cart_id = Column("cart_id", Integer) # strani kljuc
    # is it necessary to include user_id?

    #user_id = Column("user_id", Integer, ForeignKey('user.id')) """