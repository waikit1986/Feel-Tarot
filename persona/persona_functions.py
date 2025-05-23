from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from .models_persona import Persona
from .schema_persona import PersonaBase


def create_persona(db: Session, user_id: str, request: PersonaBase):
    new_profile = Persona(
        id=user_id,
        username=request.username,
        age=request.age,
        bio=request.bio
    )
    db.add(new_profile)
    
    
    db.commit()
    db.refresh(new_profile)
    return new_profile

def get_persona(db: Session, user_id: str):
    persona = db.query(Persona).filter(Persona.id == user_id).first()
    if not persona:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Persona for user {user_id} not found')
    return persona 

def get_persona_by_username(db: Session, username: str):
    persona = db.query(Persona).filter(Persona.username == username).first()
    if not persona:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Persona with username {username} not found')
    return persona

def update_persona(db: Session, user_id: str, request: PersonaBase):
    persona_query = db.query(Persona).filter(Persona.id == user_id)
    persona = persona_query.first()
    if not persona:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Persona for user {user_id} not found')

    update_data = request.dict(exclude_unset=True)
    persona_query.update(update_data)
    db.commit()
    return 'ok'

def delete_persona(db: Session, user_id: str):
    persona = db.query(Persona).filter(Persona.id == user_id).first()
    if not persona:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Persona for user {user_id} not found')
    db.delete(persona)
    db.commit()
    return 'ok'
