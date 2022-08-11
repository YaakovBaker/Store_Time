from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database import engine
import models
from routers import item, user, store

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(item.router)
app.include_router(store.router)
app.include_router(user.router)


@app.get("/")
def root():
    return RedirectResponse("/docs")







#for debugging purposes
#if __name__ == "__main__":
    #import uvicorn
    #uvicorn.run(app, host="localhost:127.0.0.1", port=9000)