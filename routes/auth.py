from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import or_
from starlette.responses import JSONResponse
from utils import oauth2, users
from schemas.users import UserNew, User, Userout
from database.database import get_db
from database import database, models
from random import randint
from sqlalchemy.sql.expression import text
from database.config import settings
from datetime import datetime, timedelta
from jose import jwt
import random
import string

router = APIRouter(prefix="/auth",tags=['Authentication'])
# Constants
JWT_SECRET = "your-secret-key"
JWT_ALGORITHM = "HS256"
OTP_EXPIRY_MINUTES = 5

@router.post("/register", response_model=Userout)
async def register( user: UserNew, db: Session=Depends(get_db)):
    hashed_password = users.hash(user.password)
    user = user.dict()
    user["password"] = hashed_password
    new_user= models.User(**user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    user_data = {
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }
    return user_data


@router.post("/login")
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(or_(models.User.email == user_credentials.username)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not users.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")
    
    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}


