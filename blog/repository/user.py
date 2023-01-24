from .. import schemas,models
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..helpers import *

def get_all(db: Session):
    blogs = db.query(models.User).all()
    
    return blogs

def create(db: Session, request):
    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    
    db.add(new_user)
    
    db.commit()
    
    db.refresh(new_user)
    
    return new_user

def get_by_id(db: Session, id):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not available")
    
    return user