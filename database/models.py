from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base

class User(Base):
    """This is The table that Stores User's information"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    bitcoin_traders = relationship("Bitcoin", back_populates="owner")

class Bitcoin(Base):
    __tablename__ = "bitcoins"
    id = Column(Integer, primary_key=True, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    symbol_id = Column(String)
    time_exchange = Column(TIMESTAMP)
    time_coinapi = Column(TIMESTAMP)
    uuid = Column(String)
    price = Column(Integer)
    size = Column(Integer)
    taker_side = Column(String)
    post_text = Column(String, index=True)

    owner = relationship("User", back_populates="bitcoin_traders")