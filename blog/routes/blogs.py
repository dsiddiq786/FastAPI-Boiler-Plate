from fastapi import APIRouter,HTTPException,Depends,status, Response
from .. import schemas,models, oauth2
from ..database import engine, SessionLocal,get_db
from ..helpers import *
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog as blogrepo

router = APIRouter(
    tags=['Blogs'],
    prefix="/blog",
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.Blog_response])
def get_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    
    return blogrepo.get_all(db)
    
@router.get('/{id}',  status_code=status.HTTP_200_OK, response_model=schemas.Blog_response)
def get_blog_by_id(id : int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogrepo.get_by_id(db,id)
    
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(blog:schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogrepo.create(db,blog)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogrepo.destroy_by_id(db,id)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, blog: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogrepo.update_by_id(db,id,blog)