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