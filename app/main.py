from fastapi import FastAPI
from app.routes import cart,orders,payment,products,reviews,saved,users

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


