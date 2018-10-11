from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()


class Account(Base):
    __tablename__ = 'account'

    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    email = Column(String(80) , nullable=False)

engine = create_engine('sqlite:///accounts.db')
 

Base.metadata.create_all(engine)
