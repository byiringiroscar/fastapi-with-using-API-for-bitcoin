from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import or_
from starlette.responses import JSONResponse
from utils import oauth2
from schemas import users as schema
from database.database import get_db
from database.models import User, Bitcoin
from sqlalchemy.sql.expression import text
from utils import users as utils
from database.config import settings
from utils.bitcoinapi import get_bitcoin_trader



router = APIRouter(prefix="/bitcoin", tags=["Bitcoin traders"])

@router.get("/")
async def get_bitcoin(db: Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    bitcoins = db.query(Bitcoin).filter_by(owner_id=current_user.id).all()
    return bitcoins

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_bitcoin(db: Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    bitcoins_data = await get_bitcoin_trader()
    for data in bitcoins_data:
        bitcoin = Bitcoin(
            owner_id=current_user.id,
            symbol_id=data["symbol_id"],
            time_exchange=data["time_exchange"],
            time_coinapi=data["time_coinapi"],
            uuid=data["uuid"],
            price=data["price"],
            size=data["size"],
            taker_side=data["taker_side"]
        )
        db.add(bitcoin)
    db.commit()
    db.refresh(current_user)
    return {"detail": "Bitcoin trader created successfully"}

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_bitcoin_by_id(id: int, db: Session = Depends(get_db), current_user: schema.User = Depends(oauth2.get_current_user)):
    bitcoin = db.query(Bitcoin).filter_by(id=id, owner_id=current_user.id).first()
    if not bitcoin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Bitcoin trader with id {id} not found")
    return bitcoin
