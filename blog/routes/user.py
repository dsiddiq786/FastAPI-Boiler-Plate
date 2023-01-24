from fastapi import APIRouter,HTTPException,Depends,status, Response
from .. import schemas,models
from ..database import engine, SessionLocal,get_db
from typing import List
from sqlalchemy.orm import Session
from ..helpers import *
from ..repository import user as userRepo

router = APIRouter(
    tags=['Users'],
    prefix="/users",
)


@router.post('/',response_model=schemas.User_response, tags=['Users'])
def create_user(request: schemas.User ,db: Session = Depends(get_db)):
    
    return userRepo.create(db,request)

@router.get('/{id}',  status_code=status.HTTP_200_OK, response_model=schemas.User_response, tags=['Users'])
def show_user(id : int, response: Response, db: Session = Depends(get_db)):
    
    return userRepo.get_by_id(db,id)