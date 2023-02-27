from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os
import uuid
from pydantic import BaseModel
import models


class CreateUser(BaseModel):
    fullname: str
    email: str
    password: str
    phone: str

IMAGEDIR = "images/"

app = FastAPI()

@app.post("/create/user")
async def create_new_user(create_user:CreateUser):
    create_user_model = models.Users()
    create_user_model.fullname = create_user.fullname
    create_user_model.email = create_user.email
    create_user_model.password = create_user.password
    create_user_model.phone = create_user.phone

    return create_user_model


@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
 
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()
 
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)
 
    return {"filename": file.filename}
