from fastapi import Depends, FastAPI, HTTPException, Cookie
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

@app.post("/items/", response_model=schemas.ItemCreate)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@app.post("/store/", response_model=schemas.StoreCreate)
def create_store(store: schemas.StoreCreate, db: Session = Depends(get_db)):
    return crud.create_store(db=db, store=store)





#for debugging purposes
#if __name__ == "__main__":
    #import uvicorn
    #uvicorn.run(app, host="localhost:127.0.0.1", port=9000)