from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str

class UserNew(User):
    password: str

class Userout(User):
    id: int
