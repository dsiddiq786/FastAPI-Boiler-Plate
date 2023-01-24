from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..helpers import *
from ..token import create_access_token

router = APIRouter(
    tags=["Authentication"]
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username)
    
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentails")
    
    if Hash.verify(user.first().password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Password is not correct")
    
    # Generate a jwt token and return it
    access_token = create_access_token(data={"sub":user.first().email})

    return {"access_token": access_token, "token_type": "bearer"}