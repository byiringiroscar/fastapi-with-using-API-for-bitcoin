from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import or_
from starlette.responses import JSONResponse
from utils import oauth2
from schemas import users as schema
from database.database import get_db
from database import database, models
from sqlalchemy.sql.expression import text
from utils import users as utils
from database.config import settings


router = APIRouter(prefix="/pay", tags=["Bit-coin"])

@router.get("/")
async def get_payments(db: Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    """
    A route to get payments made by the current user
    """
    return {"payments": []}