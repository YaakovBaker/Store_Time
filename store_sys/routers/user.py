from sys import prefix
from fastapi import APIRouter, Query, Depends, status, HTTPException, Response
import schemas, database
from typing import List
from sqlalchemy.orm import Session
from repository import user
from routers import oauth2

router = APIRouter(
    prefix = "/user",
    tags=["user"]
)

get_db = database.get_db

#POST User Methods
@router.post("/", response_model=schemas.UserShow, status_code=status.HTTP_201_CREATED)
def create_user(userI: schemas.UserCreate, db: Session = Depends(get_db), item_id: int = Query(default=None, description="Item id to add to user's cart", ge = 1)):
    return user.create_user(db=db, user=userI, item_id=item_id)
    
#GET User Methods
@router.get("/{user_id}", response_model=schemas.UserShow)
def get_user(user_id: int, db: Session = Depends(get_db), current_user: schemas.UserShow = Depends(oauth2.get_current_user)):
    return user.get_user(db=db, user_id=user_id)

#DELETE User Methods
@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user.delete_user(db=db, user_id=user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#UPDATE User Methods
@router.put("/update/{user_id}", status_code=status.HTTP_202_ACCEPTED)
def update_user(user_id: int, userI: schemas.UserUpdate, db: Session = Depends(get_db)):
    user.update_user(db=db, user_id=user_id, user=userI)
    return Response(status_code=status.HTTP_202_ACCEPTED, content="User updated")