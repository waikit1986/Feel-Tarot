from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


# class AiRequest(BaseModel):
#   card: str
#   input_text: str

# class AiResponse(BaseModel):
#   emotion: str
#   answer: str
#   class Config():
#     from_attributes = True

class AiRequest(BaseModel):
   tradition: str
   input_text: str

class AiResponse(BaseModel):
   sutra_name: str
   sutra_excerpt: str
   saint: str
   advice: str
   practice: str
   class Config():
     from_attributes = True