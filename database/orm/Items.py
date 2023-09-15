from sqlalchemy import Column, String, Integer, CHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Items(Base):
    __tablename__ = "items"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    price = Column("price", Integer) # maybe float?
    quantity = Column("quantity", Integer)
    cart_id = Column(Integer, ForeignKey("cart.id"))
    

    #cart_id = Column("cart_id", Integer) # strani kljuc
    # is it necessary to include user_id?

    #user_id = Column("user_id", Integer, ForeignKey('user.id'))

    def __init__(self, id, name, price, quantity, cart_id):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.cart_id = cart_id




    
