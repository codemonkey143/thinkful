from bicycles import bicycle
from bikeshops import bikeshop
from customers import customer

def main():
    
    print ("Hey I am main method")
    uday = bikeshop("racing",30,40,90,20,500)
    uday.bicycle_model()
    uday.final_price()

    uday = customer("racing",30,40)
    uday.customer_inventory()
    uday.purchased_bikes("uday",1800,"racing")
    uday.purchased_bikes("ramesh",1200,"folding")
    uday.purchased_bikes("srinu",700,"human-powered")
    uday.total_profit()
    uday.remaining_stock()
    
if __name__ == '__main__':
    main()
