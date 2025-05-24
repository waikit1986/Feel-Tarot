from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from .schema_user import UserBase, UserDisplay
from . import user_functions
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix='/user',
    tags=['User'],
)

@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return user_functions.create_user(db, request)

@router.get('/{id}', response_model=UserDisplay)
def get_user(id: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return user_functions.get_user(db, id)

@router.get('/{name}', response_model=UserDisplay)
def get_user_by_name(name: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)): 
    return user_functions.get_user_by_name(db, name)

@router.put('/{id}', response_model=str)
def update_user(id: str, request: UserBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return user_functions.update_user(db, id, request)

@router.delete('/{id}', response_model=str)
def delete_user(id: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return user_functions.delete_user(db, id)

