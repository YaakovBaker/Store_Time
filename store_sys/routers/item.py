from fastapi import APIRouter, Query, Depends, status, HTTPException, Response
import schemas, database, models, crud
from typing import List
from sqlalchemy.orm import Session



router = APIRouter()


#POST Item Methods
@router.post("/items/", response_model=schemas.ItemCreate, status_code=status.HTTP_201_CREATED, tags=["items"])
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    return crud.create_item(db=db, item=item)

#GET Item Methods
@router.get("/items/get_all", response_model=List[schemas.ItemShow], tags=["items"])
def get_all_items(db: Session = Depends(database.get_db), limit: int = Query(100, ge=0, le=100, description="How many items to return at most.")):
    return crud.get_items(db=db, limit=limit)


@router.get("/items/{item_id}", response_model=schemas.ItemShow, status_code=status.HTTP_200_OK, tags=["items"])
def get_item(item_id: int, response: Response, db: Session = Depends(database.get_db)):
    return_item = crud.get_item(db=db, item_id=item_id)

    if not return_item:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"Item with id {item_id} was not found")
    
    return return_item

#DELETE Item Methods
@router.delete("/items/delete/{item_id}", tags=["items"])
def delete_item(item_id: int, db: Session = Depends(database.get_db)):
    crud.delete_item(db=db, item_id=item_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#UPDATE Item Methods
@router.put("/items/update/{item_id}", status_code=status.HTTP_202_ACCEPTED, tags=["items"])
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(database.get_db)):
    crud.update_item(db=db, item_id=item_id, item=item)
    return Response(status_code=status.HTTP_202_ACCEPTED, content="Item updated")