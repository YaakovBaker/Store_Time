from typing import List
from fastapi import Depends, FastAPI, HTTPException, Cookie, Query, status, Response
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import schemas, crud, models



models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return RedirectResponse("/docs")

#Item Methods

#POST Item Methods
@app.post("/items/", response_model=schemas.ItemCreate, status_code=status.HTTP_201_CREATED, tags=["items"])
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

#GET Item Methods
@app.get("/items/get_all", response_model=List[schemas.ItemShow], tags=["items"])
def get_all_items(db: Session = Depends(get_db), limit: int = Query(100, ge=0, le=100, description="How many items to return at most.")):
    return crud.get_items(db=db, limit=limit)

@app.get("/items/{item_id}", response_model=schemas.ItemShow, status_code=status.HTTP_200_OK, tags=["items"])
def get_item(item_id: int, response: Response, db: Session = Depends(get_db)):
    return_item = crud.get_item(db=db, item_id=item_id)

    if not return_item:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f"Item with id {item_id} was not found")
    
    return return_item

#DELETE Item Methods
@app.delete("/items/delete/{item_id}", tags=["items"])
def delete_item(item_id: int, db: Session = Depends(get_db)):
    crud.delete_item(db=db, item_id=item_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#UPDATE Item Methods
@app.put("/items/update/{item_id}", status_code=status.HTTP_202_ACCEPTED, tags=["items"])
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    crud.update_item(db=db, item_id=item_id, item=item)
    return Response(status_code=status.HTTP_202_ACCEPTED, content="Item updated")


#Store Methods

#POST Store Methods
@app.post("/store/", response_model=schemas.StoreCreate, status_code=status.HTTP_201_CREATED, tags=["store"])
def create_store(store: schemas.StoreCreate, db: Session = Depends(get_db)):
    return crud.create_store(db=db, store=store)

#GET Store Methods
@app.get("/store/get_all", response_model=List[schemas.StoreShow], tags=["store"])
def get_all_stores(db: Session = Depends(get_db), limit: int = Query(100, ge=0, le=100, description="How many items to return at most.")):
    return crud.get_stores(db=db, limit=limit)

@app.get("/store/{store_id}", response_model=schemas.StoreShow,tags=["store"])
def get_store(store_id: int, db: Session = Depends(get_db)):
    return crud.get_store(db=db, store_id=store_id)

#DELETE Store Methods
@app.delete("/store/delete/{store_id}", tags=["store"])
def delete_store(store_id: int, db: Session = Depends(get_db)):
    crud.delete_store(db=db, store_id=store_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#UPDATE Store Methods
@app.put("/store/update/{store_id}", status_code=status.HTTP_202_ACCEPTED, tags=["store"])
def update_store(store_id: int, store: schemas.StoreUpdate, db: Session = Depends(get_db)):
    crud.update_store(db=db, store_id=store_id, store=store)
    return Response(status_code=status.HTTP_202_ACCEPTED, content="Store updated")



#User Methods

#POST User Methods
@app.post("/user/", response_model=schemas.UserShow, status_code=status.HTTP_201_CREATED, tags=["user"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/user/{user_id}", response_model=schemas.UserShow, tags=["user"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db=db, user_id=user_id)









#for debugging purposes
#if __name__ == "__main__":
    #import uvicorn
    #uvicorn.run(app, host="localhost:127.0.0.1", port=9000)