from fastapi import FastAPI
from .routers import product,customer,order,auth
from .database import engine
from . import models


app = FastAPI()


models.Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(product.router)
app.include_router(customer.router)
app.include_router(order.router)


@app.get("/")
def index():
    return "Hello World"