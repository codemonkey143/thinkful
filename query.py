from tbay import User,Item,Bid,session

# Returns the first user

usermodel = session.query(User.username,User.password).order_by(User.username).all()
print (usermodel)

item = session.query(Item.description).filter(Item.id >=13).all()
print (item)

user = session.query(User).first()
print (user)

user1 = session.query(User.username).first()
print (user1)
#user.username = "uday1"
#session.commit()