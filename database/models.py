from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Phonebook(Base):
    # Table name
    __tablename__ = "phonebook"

    # Table columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), unique=True, nullable=False)
    number = Column(String(9), nullable=False)
