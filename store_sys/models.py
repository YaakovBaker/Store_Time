from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    money = Column(Float, default=0.0)

    item_cart = relationship("Item", back_populates="users")
    item_id = Column(Integer, ForeignKey("items.item_id"))


class Item(Base):
    __tablename__ = "items"

    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    description = Column(String)
    tax = Column(Float)
    image_url = Column(String)

    stores = relationship("Store", back_populates="inventory")
    users = relationship("User", back_populates="item_cart")
    #barcodes = relationship("ItemRef", back_populates="reference")

class Store(Base):
    __tablename__ = "stores"

    store_id = Column(Integer, primary_key=True, index=True)
    store_name = Column(String)
    store_type = Column(String)
    
    inventory = relationship("Item", back_populates="stores")
    item_id = Column(Integer, ForeignKey("items.item_id"))

    address = Column(String, default = None)
    city = Column(String, default = None)
    state = Column(String, default = None)
    zip = Column(String, default = None)

    phone = Column(String)
    email = Column(String)
    url = Column(String)

    hours = Column(String, default = None)
    notes = Column(String, default = None)

    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    active = Column(Boolean, default=True)


#class ItemRef(Base):
    #__tablename__ = "item_ref"

    #item_ref_id = Column(Integer, primary_key=True, index=True)
    #barcode = Column(String)
    #reference = relationship("Item", back_populates="item_ref")
    #item_id = Column(Integer, ForeignKey("items.item_id"))
