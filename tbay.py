from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime,Float

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
    '''
    Challenge: Create the usermodel & bidmodels
    Try to create the two further models which you will use for the auction site.The user model should contain three columns:
    usermodel
    integer id,which is the primary key
    A username string, which cannot be null 
    A password string, which cannot be null
    
    The bid model(should contain two columns) 
    An integer id, which is the primary key 
    A floating-point price, which cannot be null
    '''
    
    
    __tablename__ = "bidmodel"
    id = Column(Integer,primary_key=True)
    price = Column(Float,nullable=False)
    
    __tablename__ = "usermodel"
    id = Column(Integer,primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    
Base.metadata.create_all(engine)
    
