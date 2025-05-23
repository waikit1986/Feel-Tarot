from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db

from .schema_persona import PersonaBase, PersonaDisplay
from . import persona_functions
from user.schema_user import UserBase
from auth.oauth2 import oauth2_scheme, get_current_user


router = APIRouter(
    prefix="/persona",
    tags=["Persona"]
)

@router.post('/', response_model=PersonaDisplay)
def create_persona(request: PersonaBase, user_id: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return persona_functions.create_persona(db, user_id, request)

@router.get('/{id}', response_model=PersonaDisplay)
def get_persona(id: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return persona_functions.get_persona(db, id)

@router.get('/{username}', response_model=PersonaDisplay)
def get_persona_by_username(username: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return persona_functions.get_persona_by_username(db, username)

@router.put('/{id}', response_model=str)
def update_persona(id: str, request: PersonaBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return persona_functions.update_persona(db, id, request)

@router.delete('/{id}', response_model=str)
def delete_persona(id: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return persona_functions.delete_persona(db, id)
