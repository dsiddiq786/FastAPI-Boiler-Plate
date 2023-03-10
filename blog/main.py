from fastapi import FastAPI, Depends , status, Response, HTTPException
from . import schemas,models
from .database import engine,get_db
from sqlalchemy.orm import Session
from typing import List
from .helpers import *
from .routes import blogs,user,authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blogs.router)
app.include_router(user.router)
app.include_router(authentication.router)
