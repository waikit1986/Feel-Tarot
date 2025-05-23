from fastapi import APIRouter, Depends, HTTPException, status
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

@router.get('/{username}', response_model=UserDisplay)
def get_user_by_name(username: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)): 
    return user_functions.get_user_by_username(db, username)

@router.put('/{username}', response_model=str)
def update_user(username: str, request: UserBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    if username != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You cannot update another user's details"
        )
    return user_functions.update_user(db, username, request)

@router.delete('/{username}', response_model=str)
def delete_user(username: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    if username != current_user.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You cannot delete another user's account"
        )
    return user_functions.delete_user(db, username)

