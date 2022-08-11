from fastapi import APIRouter, Query, Depends, status, HTTPException, Response
import schemas, database, crud
from typing import List
from sqlalchemy.orm import Session

router = APIRouter()


#POST User Methods
@router.post("/user/", response_model=schemas.UserShow, status_code=status.HTTP_201_CREATED, tags=["user"])
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db), item_id: int = Query(..., description="Item id to add to user's cart", ge = 1)):
    return crud.create_user(db=db, user=user, item_id=item_id)
    
#GET User Methods
@router.get("/user/{user_id}", response_model=schemas.UserShow, tags=["user"])
def get_user(user_id: int, db: Session = Depends(database.get_db)):
    return crud.get_user(db=db, user_id=user_id)

#DELETE User Methods
@router.delete("/user/delete/{user_id}", tags=["user"])
def delete_user(user_id: int, db: Session = Depends(database.get_db)):
    crud.delete_user(db=db, user_id=user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#UPDATE User Methods
@router.put("/user/update/{user_id}", status_code=status.HTTP_202_ACCEPTED, tags=["user"])
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(database.get_db)):
    crud.update_user(db=db, user_id=user_id, user=user)
    return Response(status_code=status.HTTP_202_ACCEPTED, content="User updated")