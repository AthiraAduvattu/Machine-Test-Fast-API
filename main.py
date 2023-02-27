from fastapi import FastAPI, Depends
import models
from database import engine
from sqlalchemy.orm import Session

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def create_database():
    return {"Database":"Created"}