from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from .. import models,schemas
from ..database import get_db

router = APIRouter(
    prefix="/api/customers",
    tags=["Customer"]
)


@router.post('/')
def register_customer(request:schemas.Customer, db:Session=Depends(get_db)):
    new_customer = models.Customer(**request.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer


@router.get('/')
def get_all_customer(db:Session=Depends(get_db)):
    customer = db.query(models.Customer).all()
    if not customer:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No products found")
    return customer

