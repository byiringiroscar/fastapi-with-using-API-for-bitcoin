from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import auth
from database import models
from database.database import engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

origin = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE", "PATCH"],
    allow_headers=["Authorization" "content-type", "Access-Control-Allow-Origin"],
)

app.include_router(auth.router)
# app.include_router(pay.router)