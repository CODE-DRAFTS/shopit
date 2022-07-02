from fastapi import FastAPI
from app.routes import cart,orders,payment,products,reviews,saved,users
from . import model
from .database import engine, get_db
from os import environ
from datetime import date


model.Base.metadata.create_all(bind=engine)  #converts models into db tables




app = FastAPI()

#CORS

#routes
app.include_router( users.router)
app.include_router( cart.router)
app.include_router( orders.router)
app.include_router( payment.router)
app.include_router( products.router)
app.include_router( reviews.router)
app.include_router( saved.router)


@app.get('/')
def home():
    return {'home template'}


