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

#Item Schemas
class ItemBase(BaseModel):
    name: str
    price: float
    tax: Union[float, None] = None

class ItemCreate(ItemBase):
    image_url: str
    barcode: str

    class Config:
        orm_mode = True

class ItemUpdate(ItemBase):
    price: float
    tax: Union[float, None] = None
    image_url: str
    barcode: str
    class Config:
        orm_mode = True

class ItemShow(ItemBase):
    name: str
    price: float
    #description: str
    image_url: str
    barcode: str

    class Config:
        orm_mode = True


#Store Schemas

class StoreBase(BaseModel):
    store_name: str
    store_type: StoreType

class StoreCreate(BaseModel):
    inventory: List[int]

    country: Union[str, None] = None
    region: Union[str, None] = None
    city: Union[str, None] = None
    #address: Union[str, None] = None
    #zip: Union[str, None] = None

    phone: str
    email: str
    url: str

    hours: Union[str, None] = None
    
    created_at: datetime
    updated_at: datetime
    active: Union[bool, None] = True

    class Config:
        orm_mode = True



class StoreUpdate(BaseModel):
    
    store_name: Union[str, None] = None
    store_type: Union[StoreType, None] = None

    inventory: List[int]

    country: Union[str, None] = None
    region: Union[str, None] = None
    city: Union[str, None] = None
    #address: Union[str, None] = None
    #zip: Union[str, None] = None

    phone: Union[str, None] = None
    email: Union[str, None] = None
    url: Union[str, None] = None

    hours: Union[str, None] = None

    updated_at: Union[datetime, None] = None
    active: Union[bool, None] = True

    class Config:
        orm_mode = True

class StoreShow(BaseModel):
    
    store_name: str
    store_type: StoreType
    
    inventory: List[int]

    country: Union[str, None] = None
    region: Union[str, None] = None
    city: Union[str, None] = None
    #address: Union[str, None] = None
    #zip: Union[str, None] = None
    
    phone: str
    email: str
    url: str
    
    hours: str

    class Config:
        orm_mode = True


#User Schemas
class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str


class UserCreate(UserBase):
    password: str
    is_active: Union[bool, None] = True
    money: Union[float, None] = 0.0

    cart: Union[ItemCreate, None] = None

    country: Union[str, None] = None
    region: Union[str, None] = None
    city: Union[str, None] = None
    #address: Union[str, None] = None
    #zip: Union[str, None] = None

    class Config:
        orm_mode = True

class UserShow(UserBase):
    first_name:str
    last_name:str
    email:str
    money:float
    cart: List[int]
    
    country: Union[str, None] = None
    region: Union[str, None] = None
    city: Union[str, None] = None
    #address: Union[str, None] = None
    #zip: Union[str, None] = None
    class Config:
        orm_mode = True

class UserUpdate(UserBase):
    first_name: str
    last_name: str
    email: str
    password: str
    is_active: Union[bool, None] = True
    money: Union[float, None] = None
    cart: Union[ItemUpdate, None] = None

    country: Union[str, None] = None
    region: Union[str, None] = None
    city: Union[str, None] = None
    #address: Union[str, None] = None
    #zip: Union[str, None] = None
    class Config:
        orm_mode = True
        

#Login

class Login(BaseModel):
    username: str
    password: str


#JWT TOekn

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None