from fastapi import APIRouter, Query, Depends, status, HTTPException, Response
import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from repository import store
from routers import oauth2

router = APIRouter(
    prefix = "/store",
    tags=["store"]
)

get_db = database.get_db

#POST Store Methods
@router.post("/", response_model=schemas.StoreCreate, status_code=status.HTTP_201_CREATED)
def create_store(storeI: schemas.StoreCreate, db: Session = Depends(get_db), item_id = Query(..., description="Item id to add to store inventory"), ge=1):
    return store.create_store(db=db, store=storeI, item_id=item_id)

#GET Store Methods
@router.get("/get_all", response_model=List[schemas.StoreShow])
def get_all_stores(db: Session = Depends(get_db), limit: int = Query(100, ge=0, le=100, description="How many items to return at most."), current_user: schemas.UserShow = Depends(oauth2.get_current_user)):
    return store.get_stores(db=db, limit=limit)

@router.get("/{store_id}", response_model=schemas.StoreShow)
def get_store(store_id: int, db: Session = Depends(get_db), current_user: schemas.UserShow = Depends(oauth2.get_current_user)):
    return store.get_store(db=db, store_id=store_id)

#DELETE Store Methods
@router.delete("/delete/{store_id}")
def delete_store(store_id: int, db: Session = Depends(get_db)):
    store.delete_store(db=db, store_id=store_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#UPDATE Store Methods
@router.put("/update/{store_id}", status_code=status.HTTP_202_ACCEPTED)
def update_store(store_id: int, storeI: schemas.StoreUpdate, db: Session = Depends(get_db)):
    store.update_store(db=db, store_id=store_id, store=storeI)
    return Response(status_code=status.HTTP_202_ACCEPTED, content="Store updated")