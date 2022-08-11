from enum import Enum
from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class StoreType(str, Enum):
    """
    StoreType is an enum that represents the type of store.
    """
    physical = "physical"
    online = "online"
    warehouse = "warehouse"


class ItemCreate(BaseModel):
    
    name: str
    price: float
    quantity: int
    description: Union[str, None] = None
    tax: Union[float, None] = None
    image_url: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Foo",
                "price": 10.0,
                "quantity": 10,
                "description": "This is a description",
                "tax": 0.05,
                "image_url": "https://example.com/image.png",
            }
        }

class ItemUpdate(BaseModel):
    price: float
    quantity: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "price": 20.0,
                "quantity": 20
            }
        }

class ItemShow(BaseModel):
    name: str
    price: float
    quantity: int
    description: str
    image_url: str

    class Config:
        orm_mode = True

class StoreCreate(BaseModel):

    store_name: str
    store_type: StoreType

    #items: List[Item] = []

    address: Union[str, None] = None
    city: Union[str, None] = None
    state: Union[str, None] = None
    zip: Union[str, None] = None

    phone: str
    email: str
    url: str

    hours: Union[str, None] = None
    notes: Union[str, None] = None
    
    created_at: datetime
    updated_at: datetime
    active: Union[bool, None] = True

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "store_name": "Foo",
                "store_type": "physical",
                #"items": [
                #    {
                #        "name": "Foo",
                #        "price": 10.0,
                #        "quantity": 10,
                #        "description": "This is a description",
                #        "tax": 0.05,
                #        "image_url": "https://example.com/image.png",
                #    }
                #]
                "address": "123 Main St",
                "city": "Los Angeles",
                "state": "CA",
                "zip": "12345",
                "phone": "123-456-7890",
                "email": "example@gmail.com",
                "url": "https://example.com",
                "hours": "Mon-Fri: 9am-5pm",
                "notes": "This is a note",
                "created_at": "2020-01-01T00:00:00",
                "updated_at": "2020-01-01T00:00:00",
                "active": True,
            }
        }

class StoreUpdate(BaseModel):
    
    store_name: Union[str, None] = None
    store_type: Union[StoreType, None] = None

    #items: List[Item] = []

    address: Union[str, None] = None
    city: Union[str, None] = None
    state: Union[str, None] = None
    zip: Union[str, None] = None

    phone: Union[str, None] = None
    email: Union[str, None] = None
    url: Union[str, None] = None

    hours: Union[str, None] = None
    notes: Union[str, None] = None
    
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    active: Union[bool, None] = True

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "store_name": "Foo",
                "store_type": "physical",
                #"items": [
                #    {
                #        "name": "Foo",
                #        "price": 10.0,
                #        "quantity": 10,
                #        "description": "This is a description",
                #        "tax": 0.05,
                #        "image_url": "https://example.com/image.png",
                #    }
                #]
                "address": "123 Main St",
                "city": "Los Angeles",
                "state": "CA",
                "zip": "12345",
                "phone": "123-456-7890",
                "email": "example@gmail.com",
                "url": "https://example.com",
                "hours": "Mon-Fri: 9am-5pm",
                "notes": "This is a note",
                "created_at": "2020-01-01T00:00:00",
                "updated_at": "2020-01-01T00:00:00",
                "active": True,
            }
        }

class StoreShow(BaseModel):
    
    store_name: str
    store_type: StoreType
    
    address: str
    city: str
    state: str
    zip: str
    
    phone: str
    email: str
    url: str
    
    hours: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "store_name": "Foo",
                "store_type": "physical",
                "address": "123 Main St",
                "city": "Los Angeles",
                "state": "CA",
                "zip": "12345",
                "phone": "123-456-7890",
                "email": "example@gmail.com",
                "url": "https://example.com",
                "hours": "Mon-Fri: 9am-5pm"
            }
        }


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    is_active: Union[bool, None] = True
    money: Union[float, None] = 0.0
    #items: List[ItemCreate] = []

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "example@gmail.com",
                "password": "password"#,
                #"is_active": True,
                #"money": 0.0
                #"items": [
                #    {
                #        "name": "Foo",
                #        "price": 10.0,
                #        "quantity": 10,
                #        "description": "This is a description",
                #        "tax": 0.05,
                #        "image_url": "https://example.com/image.png",
                #    }
                #]
            }
        }


class ItemRef(BaseModel):
    """
    ItemRef is a refrence for barcode scanners that when a barcode is scanned one can
    find the associated item in the store.
    """
    item_id: int
    #barcode to item ditionary
    barcode: str
    item: ItemCreate

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "item_id": 1,
                "barcode": "123456789",
                "item": {
                    "name": "Foo",
                    "price": 10.0,
                    "quantity": 10,
                    "description": "This is a description",
                    "tax": 0.05,
                    "image_url": "https://example.com/image.png",
                }
            }
        }