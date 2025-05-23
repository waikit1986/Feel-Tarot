from fastapi import FastAPI

from db.database import engine
from user import models_user
from user.router_user import router as UserRouter
from persona import models_persona
from persona.router_persona import router as PersonaRouter
from auth import authentication


app = FastAPI()
app.include_router(UserRouter)
app.include_router(PersonaRouter)
app.include_router(authentication.router)

@app.get("/")
def index():
    return {"message": "It's, Feel Tarot!"}

models_user.Base.metadata.create_all(bind=engine)
models_persona.Base.metadata.create_all(bind=engine)