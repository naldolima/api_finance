from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from schemas.user import UserCreate,ShowUser
from db.session import get_db
from db.repository.user import create_new_user
from db.models.user import User
from apis.v1.route_login import get_current_user_admin

router = APIRouter()

@router.post("/",response_model=ShowUser,status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session= Depends(get_db),current_user: User = Depends(get_current_user_admin)):
    user = create_new_user(user=user,db=db)
    return user
