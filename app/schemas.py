from pydantic import BaseModel



class Product(BaseModel):
    name:str
    description:str
    price:float
    quantity_available:int


class Customer(BaseModel):
    first_name:str
    last_name:str
    email:str
    phone:str
    address:str
    is_active:bool = True


class Order(BaseModel):
    customer_id:int
    total_amount:float
    status:str   


class Login(BaseModel):
    email:str     
    

    