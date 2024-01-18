from typing import Union
from fastapi import FastAPI

from app.db.connection import connect
from app.view.user import user_router
from app.view.login import login_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



app.include_router(user_router)
app.include_router(login_router)