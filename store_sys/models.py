from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.types import UserDefinedType
from datetime import datetime

from database import Base

class Inventory(UserDefinedType):
    cache_ok = True
    
    def __init__(self, items: list):
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)


class Item(Base):
    __tablename__ = "items"

    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    #description = Column(String)
    #tax = Column(Float)
    #image_url = Column(String)
    #barcode = Column(String(10), unique=True, nullable=False)

    #stores = relationship("Store", back_populates="inventory")
    #users = relationship("User", back_populates="cart")

class Store(Base):
    __tablename__ = "stores"

    store_id = Column(Integer, primary_key=True, index=True)
    store_name = Column(String)
    store_type = Column(String)

    inventory = Column(Inventory([]))
    
    #inventory = relationship("Item", back_populates="stores")
    #item_id = Column(Integer, ForeignKey("items.item_id"))

    #address = Column(String, default = None)
    #city = Column(String, default = None)
    #state = Column(String, default = None)
    #zip = Column(String, default = None)

    phone = Column(String)
    email = Column(String)
    #url = Column(String)

    #hours = Column(String, default = None)
    #notes = Column(String, default = None)

    #created_at = Column(DateTime, default=datetime.now())
    #updated_at = Column(DateTime, default=datetime.now())
    active = Column(Boolean, default=True)


class Cart(UserDefinedType):

    def __init__(self, items: list):
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    money = Column(Float, default=0.0)

    cart = Column(Cart([]))

    #cart = relationship("Item", back_populates="users")
    #item_id = Column(Integer, ForeignKey("items.item_id"))
