from typing import Union
from fastapi import HTTPException, Response, status
from sqlalchemy.orm import Session
from hashing import Hash
import models, schemas

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