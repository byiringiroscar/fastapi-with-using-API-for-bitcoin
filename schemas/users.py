from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str

class UserNew(User):
    password: str

class Userout(User):
    id: int

class TokenData(BaseModel):
    id: str|None = None

class Bitcoin(BaseModel):
    symbol_id: str
    time_exchange: str
    time_coinapi: str
    uuid: str
    price: float
    size: float
    taker_side: str
    post_text: str