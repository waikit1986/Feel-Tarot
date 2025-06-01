from pydantic import BaseModel


class UserBase(BaseModel):
  username: str
  email: str
  password: str

class UserDisplay(BaseModel):
  username: str
  email: str
  class Config():
    from_attributes = True
    
class UsernameDisplay(BaseModel):
  username: str
  class Config():
    from_attributes = True
