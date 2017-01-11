from bicycles import bikeshops,customers,bicycle

def main():
    print ("Hey I am main method")
    uday = bikeshops("racing",30,40,90)
    uday.bicycle_model()
    uday.final_price()

    uday = customers("racing",30,40)
    uday.customer_inventory()
    uday.purchased_bikes("uday",1800,"racing")
    uday.purchased_bikes("ramesh",1200,"folding")
    uday.purchased_bikes("srinu",700,"human-powered")
    uday.total_profit()
    uday.remaining_stock()
    
    print ("ending main method")
    
if __name__ == "__main__":
    main()
