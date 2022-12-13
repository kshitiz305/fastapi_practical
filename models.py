from sqlalchemy import ForeignKey, Column, Integer, String
from Database import Base
from sqlalchemy.orm import relationship





class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String,unique=True)
    username = Column(String,unique=True)
    firstname = Column(String,unique=True)
    todo = relationship('Todo',back_populates = "owner")

class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True)
    email = Column(String,unique=True)
    username = Column(String,unique=True)
    firstname = Column(String,unique=True)
    owner_id = Column(Integer,ForeignKey('users.id'))
    owner = relationship('User',back_relationship = 'todo')