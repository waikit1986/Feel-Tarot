from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PersonaBase(BaseModel):
    username: str
    age: Optional[int] = None
    bio: Optional[str] = None

class PersonaDisplay(BaseModel):
    username: str
    age: Optional[int]
    bio: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config():
        from_attributes = True 
