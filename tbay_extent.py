from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Integer,String,Date,Column,Table,ForeignKey,Float
from datetime import datetime

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/ebay')
Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()

#Users should be able to auction multiple items
#Users should be able to bid on multiple items
#Multiple users should be able to place a bid on an items

biditem_association_table = Table('biditem_association',Base.metadata,Column('users_id',Integer,ForeignKey('users.id'))
,Column('biditem_id',Integer,ForeignKey('biditem.id')) )

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    auctionItems = relationship('AuctionItems',backref='user')
    bidItems = relationship('BidItems',secondary='biditem_association',backref='user')
    
class AuctionItems(Base):
    __tablename__ = 'auction'
    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    #cost = Column(Integer)
    user_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    
class BidItems(Base):
    __tablename__ = 'biditem'
    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    cost = Column(Integer)
    
Base.metadata.create_all(engine)

user1 = Users(name="Beyonce")
user2 = Users(name="david")
user3 = Users(name="mohit")

#user1 following in auction1
auctionItem1 = AuctionItems(name="baseball")
user1.auctionItems.append(auctionItem1)

#auctionItem2 = AuctionItems(name="baseball")
#user1.auctionItems.append(auctionItem2)

bidItem1 = BidItems(name="baseball")
#bidItem2 = BidItems(name="cellphone",cost=700)
user1_bid = BidItems(name="baseball",cost=200)
user2_bid = BidItems(name="baseball",cost=300)
bidItem1.bidItems = [user1_bid,user2_bid]


#session.add_all([user1,user2,user3,auctionItem1,bidItem1,user1_bid,user2_bid])

#session.commit()

#print (user1.name)
#print (user2.name)

for user in user1.auctionItems:
    print (user.name)
    
#print (auctionItem1.user.name)

for bid in user1.bidItems:
    print(bid.name)
    print(bid.cost)


# Returns the first user

print ("Using psycopg2...")
import psycopg2
import logging

logging.debug("Conneccting to PostgreSQL")
connection = psycopg2.connect(database="ebay")
logging.debug("database connection established")

cursor = connection.cursor()

command = "SELECT MAX(cost) as max_bid from biditem"
cursor.execute(command)
row = cursor.fetchone()
print (row)
