from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas
from .. import models
from ..utils.verify_jwt import auth

router = APIRouter(
    prefix="/api/products",
    tags=["Products"]
)



@router.post("/")
def create_product(request:schemas.Product, db:Session=Depends(get_db),current_user:str=Depends(auth)):
     new_product = models.Product(**request.dict())
     db.add(new_product)
     db.commit()
     db.refresh(new_product)
     return new_product


@router.get("/")
def get_products(db:Session=Depends(get_db),current_user:str=Depends(auth)):
     products = db.query(models.Product).all()
     if not products:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No products found")
     return products


@router.get("/{id}")
def get_products(id:int, db:Session=Depends(get_db),current_user:str=Depends(auth)):
     product = db.query(models.Product).filter(models.Product.id == id).first()
     if not product:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No product found")
     return product



@router.put("/{id}")
def update_products(id:int, request:schemas.Product, db:Session=Depends(get_db),current_user:str=Depends(auth)):
     product = db.query(models.Product).filter(models.Product.id == id).first()
     if not product:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No product found")
     update_data = request.dict(exclude_unset=True)
     db.query(models.Product).filter(models.Product.id == id).update(update_data)
     db.commit()
     db.refresh(product)
     return product



@router.delete("/{id}")
def delete_products(id:int, db:Session=Depends(get_db),current_user:str=Depends(auth)):
     product = db.query(models.Product).filter(models.Product.id == id).first()
     if not product:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No product found")
     db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
     db.commit()
     return product