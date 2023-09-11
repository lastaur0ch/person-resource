from sqlalchemy import Column, Integer, String
from .database import Base

class Person(Base):
    __tablename__ = "persons"

    user_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=True)