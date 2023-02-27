from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class Users(Base):
    __tablename__="users"
    
    id=Column(Integer, primary_key=True, index=True)
    fullname=Column(String)
    email=Column(String)
    password=Column(String)
    phone=Column(String)