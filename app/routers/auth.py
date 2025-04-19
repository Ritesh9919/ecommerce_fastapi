from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import models,schemas
from ..database import get_db
from ..utils.jwt_token import create_access_token




router = APIRouter(
    prefix="/api/auth",
    tags=["Auth"]
)



@router.post("/login")
def login(request:schemas.Login, db:Session=Depends(get_db)):
    user = db.query(models.Customer).filter(models.Customer.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    access_token = create_access_token(data={"sub":user.email})
    return {"access_token":access_token, "token_type":"bearer"}
    
    



