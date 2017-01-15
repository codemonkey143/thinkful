from tbay import User,Item,Bid,session
    

#chnage values existing & run as python commit.py

def commit_database():
    items = Item()
    items.id = 14
    items.name = "plastic"
    items.description = "it used for"
    session.add(items)
    
    usermodel = User()
    usermodel.id = 14
    usermodel.username = "loki"
    usermodel.password= "908765"
    session.add(usermodel)
    
    bidmodel = Bid()
    bidmodel.id = 14
    bidmodel.price = 980.59
    session.add(bidmodel)
    
    session.commit()
    
    
commit_database()

