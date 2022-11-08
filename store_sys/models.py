from enum import unique
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.types import UserDefinedType
from datetime import datetime

from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    tax = Column(Float)
    image_url = Column(String)
    barcode = Column(String(10), unique=True, nullable=False)
    #inventory key that uses this object
    #cart key that uses this object

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    #in Store will have one to many here, this is many to one
    store = relationship("Store", backref=backref("inventory", uselist=False))
    store_id = Column(Integer, ForeignKey("stores.id"))
    #one to one
    item_id = Column(Integer, ForeignKey("items.id"))
    item = relationship("Item", backref=backref("inventory", uselist=False))
    quantity = Column(Integer)

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    store_name = Column(String)
    store_type = Column(String)

    #one to many
    store_inventory = relationship("Inventory", back_populates="stores")

    #make correct one to one but not bidirectional
    country = relationship("Country", back_populates="stores", uselist = False)
    region = relationship("Region", back_populates="stores", uselist = False)
    city = relationship("City", back_populates="stores", uselist = False)
    #address = Column(String, default = None)
    #zip = Column(String, default = None)

    phone = Column(String)
    email = Column(String)
    url = Column(String)

    hours = Column(String, default = None)

    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    active = Column(Boolean, default=True)

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    #one to many for user to Cart but many to one for cart to user
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref=backref("cart", uselist=False))
    #make one to one not bidirectional 
    item_id = Column(Integer, ForeignKey("items.id"))
    item = relationship("Item", backref=backref("cart", uselist=False))
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

    #make correct one to one but not bidirectional
    country = relationship("Country", back_populates="users", uselist = False)
    region = relationship("Region", back_populates="users", uselist = False)
    city = relationship("City", back_populates="users", uselist = False)
    #address = Column(String, default = None)
    #zip = Column(String, default = None)
    #one to many
    user_cart = relationship("Item", back_populates="users")

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable = False)

class Region(Base):
    __tablename__ = "regions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable = False)

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable = False)