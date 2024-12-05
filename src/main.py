from fastapi import FastAPI
from src import crud_apis
from .db import get_db, engine, Base
from .schemas import *

app = FastAPI()


@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)


app.include_router(crud_apis.router)
