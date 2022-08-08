from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    money = Column(Integer, default=0)
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    item_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(String)
    quantity = Column(Integer)
    description = Column(String, index=True)
    tax = Column(String)
    image_url = Column(String)

class Store(Base):
    __tablename__ = "stores"

    store_id = Column(Integer, primary_key=True, index=True)
    store_name = Column(String, index=True)
    store_type = Column(String, index=True)
    
    items = relationship("Item", back_populates="store")

    address = Column(String, index=True)
    city = Column(String, index=True)
    state = Column(String, index=True)
    zip = Column(String, index=True)

    phone = Column(String, index=True)
    email = Column(String, index=True)
    url = Column(String, index=True)

    hours = Column(String, index=True)
    notes = Column(String, index=True)

    created_at = Column(String, index=True)
    updated_at = Column(String, index=True)
    active = Column(Boolean, default=True)

class ItemRef(Base):
    __tablename__ = "item_ref"

    item_id = Column(Integer, primary_key=True, index=True)
    barcode = Column(String, index=True)
    item = relationship("Item", back_populates="store")
