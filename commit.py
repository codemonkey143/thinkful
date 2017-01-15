from tbay import User,Item,Bid,session
    

#chnage values existing & run as python commit.py

def commit_database():
    items = Item()
    items.id = 13
    items.name = "unlimited"
    items.description = "bodbrand"
    session.add(items)
    
    usermodel = User()
    usermodel.id = 13
    usermodel.username = "ramboo"
    usermodel.password= "duplix"
    session.add(usermodel)
    
    bidmodel = Bid()
    bidmodel.id = 13
    bidmodel.price = 500.60
    session.add(bidmodel)
    
    session.commit()
    
    
commit_database()

