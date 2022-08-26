from typing import Union
from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session
from hashing import Hash
import models, schemas

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