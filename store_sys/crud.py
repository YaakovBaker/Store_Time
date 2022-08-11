from typing import Union
from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session
from hashing import Hash
import models, schemas

#User methods

#get user methods
def get_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"User with id {user_id} was not found")
    return db_user
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

#create user methods
def create_user(db: Session, user: schemas.UserCreate, item_id: Union[int, None] = None):
    db_user = models.User(email=user.email, hashed_password=Hash.bcrypt(user.password), first_name=user.first_name, last_name=user.last_name, item_id=item_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

#Delete user methods
def delete_user(db: Session, user_id: int):
    db.query(models.User).filter(models.User.user_id == user_id).delete(synchronize_session=False)
    db.commit()

#Update user methods
def update_user(db: Session, user: schemas.UserUpdate, user_id: int):
    db_user = db.query(models.User).filter(models.User.user_id == user_id)
    if not db_user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} was not found")
    db_user.update(user.dict())
    db.commit()

#Item methods

#get item methods
def get_items(db: Session, limit: int, skip: int = 0):
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.item_id == item_id).first()

#create item methods
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

#Delete item methods
def delete_item(db: Session, item_id: int):
    db.query(models.Item).filter(models.Item.item_id == item_id).delete(synchronize_session=False)
    db.commit()

#Update item methods
def update_item(db: Session, item: schemas.ItemUpdate, item_id: int):
    db_item = db.query(models.Item).filter(models.Item.item_id == item_id)
    if not db_item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with id {item_id} was not found")
    db_item.update(item.dict())
    db.commit()


#Store methods

#get store methods
def get_stores(db: Session, limit: int, skip: int = 0):
    return db.query(models.Store).offset(skip).limit(limit).all()

def get_store(db: Session, store_id: int):
    return db.query(models.Store).filter(models.Store.store_id == store_id).first()

#create store methods
def create_store(db: Session, store: schemas.StoreCreate, item_id: Union[int, None] = None):
    db_store = models.Store(models.Store.store_name==store.store_name, models.Store.store_type==store.store_type, models.Store.item_id==item_id, models.Store.phone==store.phone, models.Store.email==store.email)
    db.add(db_store) 
    db.commit()
    db.refresh(db_store)
    return db_store

#Delete store methods
def delete_store(db: Session, store_id: int):
    db.query(models.Store).filter(models.Store.store_id == store_id).delete(synchronize_session=False)
    db.commit()

#Update store methods
def update_store(db: Session, store: schemas.StoreUpdate, store_id: int):
    db_store = db.query(models.Store).filter(models.Store.store_id == store_id)
    if not db_store.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Store with id {store_id} was not found")
    db_store.update(store.dict())
    db.commit()