from pydantic import BaseModel
from typing import List,Union

class User(BaseModel):
    name: str
    email: str
    password:str

class Blog(BaseModel):
    title:str
    body:str
    class Config():
        orm_mode = True

class User_response(BaseModel):
    name:str
    email:str
    blogs : List[Blog] = []
    class Config():
        orm_mode = True

class Blog_response(BaseModel):
    title:str
    creator: User_response
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None