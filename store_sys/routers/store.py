from fastapi import APIRouter, Query, Depends, status, HTTPException, Response
import schemas, database, models, crud
from typing import List
from sqlalchemy.orm import Session

router = APIRouter()

#POST Store Methods
@router.post("/store/", response_model=schemas.StoreCreate, status_code=status.HTTP_201_CREATED, tags=["store"])
def create_store(store: schemas.StoreCreate, db: Session = Depends(database.get_db), item_id = Query(..., description="Item id to add to store inventory"), ge=1):
    return crud.create_store(db=db, store=store, item_id=item_id)

#GET Store Methods
@router.get("/store/get_all", response_model=List[schemas.StoreShow], tags=["store"])
def get_all_stores(db: Session = Depends(database.get_db), limit: int = Query(100, ge=0, le=100, description="How many items to return at most.")):
    return crud.get_stores(db=db, limit=limit)

@router.get("/store/{store_id}", response_model=schemas.StoreShow,tags=["store"])
def get_store(store_id: int, db: Session = Depends(database.get_db)):
    return crud.get_store(db=db, store_id=store_id)

#DELETE Store Methods
@router.delete("/store/delete/{store_id}", tags=["store"])
def delete_store(store_id: int, db: Session = Depends(database.get_db)):
    crud.delete_store(db=db, store_id=store_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#UPDATE Store Methods
@router.put("/store/update/{store_id}", status_code=status.HTTP_202_ACCEPTED, tags=["store"])
def update_store(store_id: int, store: schemas.StoreUpdate, db: Session = Depends(database.get_db)):
    crud.update_store(db=db, store_id=store_id, store=store)
    return Response(status_code=status.HTTP_202_ACCEPTED, content="Store updated")