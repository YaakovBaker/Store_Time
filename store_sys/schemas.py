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
    #description: Union[str, None] = None
    #tax: Union[float, None] = None
    #image_url: str
    #barcode: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Foo",
                "price": 10.0,
                "quantity": 10#,
                #"description": "This is a description",
                #"tax": 0.05,
                #"image_url": "https://example.com/image.png",
                #"barcode": "123456789"
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
    #description: str
    #image_url: str
    #barcode: str

    class Config:
        orm_mode = True

class StoreCreate(BaseModel):

    store_name: str
    store_type: StoreType

    inventory: ItemCreate#Union[List[ItemCreate], None] = []

    #address: Union[str, None] = None
    #city: Union[str, None] = None
    #state: Union[str, None] = None
    #zip: Union[str, None] = None

    phone: str
    email: str
    #url: str

    #hours: Union[str, None] = None
    #notes: Union[str, None] = None
    
    #created_at: datetime
    #updated_at: datetime
    active: Union[bool, None] = True

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "store_name": "Foo",
                "store_type": "physical",
                "inventory": [
                    {
                        "name": "Foo",
                        "price": 10.0,
                        "quantity": 10#,
                        #"description": "This is a description",
                        #"tax": 0.05,
                        #"image_url": "https://example.com/image.png"
                    }
                ],
                #"address": "123 Main St",
                #"city": "Los Angeles",
                #"state": "CA",
                #"zip": "12345",
                "phone": "123-456-7890",
                "email": "example@gmail.com",
                #"url": "https://example.com",
                #"hours": "Mon-Fri: 9am-5pm",
                #"notes": "This is a note",
                #"created_at": "2020-01-01T00:00:00",
                #"updated_at": "2020-01-01T00:00:00",
                "active": True
            }
        }

class StoreUpdate(BaseModel):
    
    store_name: Union[str, None] = None
    store_type: Union[StoreType, None] = None

    inventory: ItemUpdate#Union[List[ItemCreate], None] = []

    #address: Union[str, None] = None
    #city: Union[str, None] = None
    #state: Union[str, None] = None
    #zip: Union[str, None] = None

    phone: Union[str, None] = None
    email: Union[str, None] = None
    #url: Union[str, None] = None

    #hours: Union[str, None] = None
    #notes: Union[str, None] = None
    
    #created_at: Union[datetime, None] = None
    #updated_at: Union[datetime, None] = None
    active: Union[bool, None] = True

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "store_name": "Foo",
                "store_type": "physical",
                "inventory": [
                    {
                        "name": "Foo",
                        "price": 10.0,
                        "quantity": 10#,
                        #"description": "This is a description",
                        #"tax": 0.05,
                        #"image_url": "https://example.com/image.png",
                        #"barcode": "123456789"
                    }
                ],
                #"address": "123 Main St",
                #"city": "Los Angeles",
                #"state": "CA",
                #"zip": "12345",
                "phone": "123-456-7890",
                "email": "example@gmail.com",
                #"url": "https://example.com",
                #"hours": "Mon-Fri: 9am-5pm",
                #"notes": "This is a note",
                #"created_at": "2020-01-01T00:00:00",
                #"updated_at": "2020-01-01T00:00:00",
                "active": True
            }
        }

class StoreShow(BaseModel):
    
    store_name: str
    store_type: StoreType
    
    inventory: ItemShow#List[ItemShow] = []

    #address: str
    #city: str
    #state: str
    #zip: str
    
    phone: str
    email: str
    #url: str
    
    #hours: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "store_name": "Foo",
                "store_type": "physical",
                "inventory": [
                    {
                        "name": "Foo",
                        "price": 10.0,
                        "quantity": 10
                    }
                ],
                #"address": "123 Main St",
                #"city": "Los Angeles",
                #"state": "CA",
                #"zip": "12345",
                "phone": "123-456-7890",
                "email": "example@gmail.com"#,
                #"url": "https://example.com",
                #"hours": "Mon-Fri: 9am-5pm"
            }
        }


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    is_active: Union[bool, None] = True
    money: Union[float, None] = 0.0
    cart: ItemCreate#List[ItemCreate] = []


    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "example@gmail.com",
                "password": "password",
                "is_active": True,
                "money": 0.0,
                "cart": [
                    {
                        "name": "Foo",
                        "price": 10.0,
                        "quantity": 10,
                        "description": "This is a description",
                        "tax": 0.05,
                        "image_url": "https://example.com/image.png",
                        "barcode": "123456789"
                    }
                ]
            }
        }

class UserShow(BaseModel):
    first_name:str
    last_name:str
    email:str
    money:float
    cart: ItemShow #need to get to work for list of items
    
    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    is_active: Union[bool, None] = True
    money: Union[float, None] = None
    cart: ItemUpdate#List[ItemCreate] = []

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "John@gmail.com",
                "password": "password",
                "is_active": True,
                "money": 0.0,
                "cart": [
                    {
                        "name": "Foo",
                        "price": 10.0,
                        "quantity": 10,
                        "description": "This is a description",
                        "tax": 0.05,
                        "image_url": "https://example.com/image.png",
                        "barcode": "1234567890123"
                    }
                ]
            }
        }