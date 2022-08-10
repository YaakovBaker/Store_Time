from typing import List
from fastapi import Depends, FastAPI, HTTPException, Cookie, Query, status
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
@app.post("/items/", response_model=schemas.ItemCreate, status_code=status.HTTP_201_CREATED)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

#GET Item Methods
@app.get("/items/get_all", response_model=List[schemas.ItemCreate])
def get_all_items(db: Session = Depends(get_db), limit: int = Query(100, ge=0, le=100, description="How many items to return at most.")):
    return crud.get_items(db=db, limit=limit)

@app.get("/items/{item_id}", response_model=schemas.ItemCreate)
def get_item(item_id: int, db: Session = Depends(get_db)):
    return crud.get_item(db=db, item_id=item_id)


#Store Methods

#POST Store Methods
@app.post("/store/", response_model=schemas.StoreCreate, status_code=status.HTTP_201_CREATED)
def create_store(store: schemas.StoreCreate, db: Session = Depends(get_db)):
    return crud.create_store(db=db, store=store)

#GET Store Methods
@app.get("/store/get_all", response_model=List[schemas.StoreCreate])
def get_all_stores(db: Session = Depends(get_db), limit: int = Query(100, ge=0, le=100, description="How many items to return at most.")):
    return crud.get_stores(db=db, limit=limit)

@app.get("/store/{store_id}", response_model=schemas.StoreCreate)
def get_store(store_id: int, db: Session = Depends(get_db)):
    return crud.get_store(db=db, store_id=store_id)



#for debugging purposes
#if __name__ == "__main__":
    #import uvicorn
    #uvicorn.run(app, host="localhost:127.0.0.1", port=9000)