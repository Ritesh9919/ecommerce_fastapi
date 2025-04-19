from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas
from .. import models

router = APIRouter(
    prefix="/api/orders",
    tags=["Orders"]
)


@router.post('/')
def create_order(request:schemas.Order, db:Session=Depends(get_db)):
    customer = db.query(models.Customer).filter(models.Customer.id == request.customer_id).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found")
    order = models.Order(**request.dict())
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
    
    