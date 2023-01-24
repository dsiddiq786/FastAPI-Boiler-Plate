from passlib.context import CryptContext
from fastapi import Header, HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_context.hash(password)
    
    def verify(hashed_password,plain_password):
        return pwd_context.verify(plain_password, hashed_password)



async def get_token_header(x_token: str = Header()):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")