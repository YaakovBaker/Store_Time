from fastapi import APIRouter, Query, Depends, status, HTTPException, Response
import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from repository import item
from routers import oauth2


router = APIRouter(
    prefix = "/items",
    tags=["item"]
)

get_db = database.get_db

#POST Item Methods
@router.post("/", response_model=schemas.ItemCreate, status_code=status.HTTP_201_CREATED)
def create_item(itemI: schemas.ItemCreate, db: Session = Depends(get_db)):
    return item.create_item(db=db, item=itemI)

#GET Item Methods
@router.get("/get_all", response_model=List[schemas.ItemShow])
def get_all_items(db: Session = Depends(get_db), limit: int = Query(100, ge=0, le=100, description="How many items to return at most."), current_user: schemas.UserShow = Depends(oauth2.get_current_user)):
    return item.get_items(db=db, limit=limit)


@router.get("/{item_id}", response_model=schemas.ItemShow, status_code=status.HTTP_200_OK)
def get_item(item_id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.UserShow = Depends(oauth2.get_current_user)):
    return_item = item.get_item(db=db, item_id=item_id)

    if not return_item:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"Item with id {item_id} was not found")
    
    return return_item

#DELETE Item Methods
@router.delete("/delete/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    item.delete_item(db=db, item_id=item_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#UPDATE Item Methods
@router.put("/update/{item_id}", status_code=status.HTTP_202_ACCEPTED)
def update_item(item_id: int, itemI: schemas.ItemUpdate, db: Session = Depends(get_db)):
    item.update_item(db=db, item_id=item_id, item=itemI)
    return Response(status_code=status.HTTP_202_ACCEPTED, content="Item updated")