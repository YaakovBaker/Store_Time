from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.types import UserDefinedType
from datetime import datetime

from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    #description = Column(String)
    tax = Column(Float)
    image_url = Column(String)
    barcode = Column(String(10), unique=True, nullable=False)

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer)
    store_id = relationship("Store", back_populates="inventory")
    quantity = Column(Integer)

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    store_name = Column(String)
    store_type = Column(String)

    inventory = relationship("Inventory", back_populates="stores")

    #address = Column(String, default = None)
    #city = Column(String, default = None)
    #state = Column(String, default = None)
    #zip = Column(String, default = None)

    phone = Column(String)
    email = Column(String)
    #url = Column(String)

    #hours = Column(String, default = None)
    #notes = Column(String, default = None)

    created_at = Column(DateTime, default=datetime.now())
    #updated_at = Column(DateTime, default=datetime.now())
    active = Column(Boolean, default=True)

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    user_id = relationship("User", back_populates="cart")
    item_id = Column(Integer)
    quantity = Column(Integer)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    money = Column(Float, default=0.0)

    cart = relationship("Item", back_populates="users")
