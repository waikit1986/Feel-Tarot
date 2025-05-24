from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status

from db.hash import Hash
from .schema_user import UserBase
from .models_user import User


def create_user(db: Session, request: UserBase):
  new_user = User(
    username = request.username,
    email = request.email,
    password = Hash.bcrypt(request.password)
  )
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

def get_user_by_id(db: Session, id: str):
  user = db.query(User).filter(User.id == id).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail='User with id {id} not found')
  return user

def update_user(db: Session, id: str, request: UserBase):
  user = db.query(User).filter(User.id == id)
  if not user.first():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail='User with id {id} not found')
  user.update({
    User.username: request.username,
    User.email: request.email,
    User.password: Hash.bcrypt(request.password)
  })
  db.commit()
  return 'ok'

def delete_user(db: Session, id: int):
  user = db.query(User).filter(User.id == id).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail='User with id {id} not found')
  db.delete(user)
  db.commit()
  return 'ok'

# def get_user_by_username(db: Session, username: str):
#   user = db.query(User).filter(User.username == username).first()
#   if not user:
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#       detail='User with username {username} not found')
#   return user

# def update_user(db: Session, username: str, request: UserBase):
#   user = db.query(User).filter(User.username == username)
#   if not user.first():
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#       detail='User with username {username} not found')
#   user.update({
#     User.username: request.username,
#     User.email: request.email,
#     User.password: Hash.bcrypt(request.password)
#   })
#   db.commit()
#   return 'ok'

