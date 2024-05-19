from typing import Union
from fastapi import FastAPI

from app.db.connection import connect
from app.view.user import user_router
from app.view.login import login_router
from app.view.doctor import doctor_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:5173",
]


app.include_router(user_router)
app.include_router(login_router)
app.include_router(doctor_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
