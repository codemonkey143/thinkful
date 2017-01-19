from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine
from sqlalchemy import Date,String,Integer,Table,ForeignKey,Column
from datetime import datetime

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    id = Column(Integer,primary_key=True)
    name = Column(String, nullable=False)
    
    guitars = relationship("Guitar", backref='manufacturer')

class Guitar(Base):
    __tablename__ = 'guitar'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String,nullable=False)
    person_id = Column(Integer,ForeignKey('manufacturer.id'),nullable=False)
    issue_date = Column(Date, nullable=False, default=datetime.utcnow)
    
Base.metadata.create_all(engine)

fender = Manufacturer(name="Fender")
#strat = Guitar(name="Stratocaster", manufacturer=fender)
#manufacturer = fender
strat = Guitar(name="Stratocaster")
tele = Guitar(name="Telecaster")
jumpt = Guitar(name="stella")
fender.guitars.append(strat)
fender.guitars.append(tele)
fender.guitars.append(jumpt)

session.add_all([fender, strat,tele,jumpt])
session.commit()

for guitar in fender.guitars:
    print(guitar.name)
print(tele.manufacturer.name)


# Steps to create One to Many Relation
# need to append child class obj to parent class instance using relationship instance  