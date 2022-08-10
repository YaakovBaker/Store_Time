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

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.Item, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@app.post("/store", response_model=schemas.Store)
def create_store(request: schemas.Store, db: Session = Depends(get_db)):
    return crud.create_store(db=db, store=request)

#@app.post("/login")
#def login( user: schemas.User, db: Session = Depends(get_db)):
#    db_user = crud.get_user_by_email(db, user.email)
#    if not db_user:
#        raise HTTPException(status_code=404, detail="User not found")
#    return {"access_token": "fake-token"}

#@app.post("/users/", response_model=schemas.User)
#def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#    db_user = crud.get_user_by_email(db, email=user.email)
#    if db_user:
#        raise HTTPException(status_code=400, detail="Email already registered")
#    return crud.create_user(db=db, user=user)


#@app.get("/users/", response_model=list[schemas.User])
#def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#    users = crud.get_users(db, skip=skip, limit=limit)
#    return users


#@app.get("/users/{user_id}", response_model=schemas.User)
#def read_user(user_id: int, db: Session = Depends(get_db)):
#    db_user = crud.get_user(db, user_id=user_id)
#    if db_user is None:
#        raise HTTPException(status_code=404, detail="User not found")
#    return db_user





#@app.get("/items/", response_model=list[schemas.Item])
#def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#    items = crud.get_items(db, skip=skip, limit=limit)
#    return items


#for debugging purposes
#if __name__ == "__main__":
    #import uvicorn
    #uvicorn.run(app, host="localhost:127.0.0.1", port=9000)