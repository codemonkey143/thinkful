from tbay import User,Item,Bid,session

# Returns the first user

usermodel = session.query(User.username,User.password).order_by(User.username).all()
#print (usermodel)

item = session.query(Item.description).filter(Item.id >=13).all()
#print (item)

user = session.query(User).all()
#print (user)

print("bellow are the key,value of the user")

for item in user:
    print (item.id,'\t',item.username ,'\t' ,item.password)
    

#for key, value in user.__dict__.iteritems():
#    print (key,value)

user1 = session.query(User).first()
print (user1)
user.username = "uday1"
session.commit()

Deleting the sessions rows
user_del = session.query(User).first()
session.delete(user_del)
session.commit()