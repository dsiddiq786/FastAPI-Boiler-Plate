from fastapi import Depends,HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .token import *

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token_: str = Depends(oauth2_scheme)):
    return verify_access_token(token_)