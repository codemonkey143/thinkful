class Bicycle(object):
    
    def __init__(self,modelName,weight,cost):
        self.modelName = modelName
        self.weight = weight
        self.cost = cost
       
    def bicycle_details(self):
        print(self.modelName)
        print(self.weight)
        print(self.cost)
        
class bikeshops(Bicycle):
    
   def __init__(self,modelName,inventory,margin,profit):
        self.modelName = modelName  
        self.inventory = inventory
        self.margin = margin
        self.profit = profit
   
   def bicycle_model(self):
        name = self.modelName.lower()
        global stock
        global weight
        stock = {
            "racing":1100,
            "folding":700,
            "BMX":900,
            "human-powered":150,
            "motor-assisted":900,
            "mountain-biking":1000
            
        }
        weight = {
            "racing":20,
            "folding":30,
            "BMX":25,
            "human-powered":10,
            "motor-assisted":45,
            "mountain-biking":15
            
        }
    
   def final_price(self):
       global updatedStock
       updatedStock = {}
       for model in stock:
           updatedStock[model] = stock[model] + 0.5 * stock[model]
    
       print ("-------------initial stock price -----------------------"+"\n"+str(stock))
       print ("-------------updated stock price------------------------"+"\n"+str(updatedStock))
       
   #ACICS
   
class customers(bikeshops):
    
    def __init__(self,name,fund,newbicycle):
        self.name = name
        self.fund = fund
        self.newbicycle = newbicycle
        
    def customer_inventory(self):
        customers = {"daniel":200,"david":500,"johny":1000}
        global customer_sheet
        customer_sheet = {}
        for key1 in customers:
            for key2 in stock:
                if customers[key1] >= stock[key2]:
                    sellPrice = stock[key2] + 0.5 * stock[key2]
                    if key1 not in customer_sheet:
                        global list1 
                        list1 = []
                        list1.append(key2)
                        list1.append(stock[key2] + 0.5 * stock[key2])
                        list1.append(sellPrice - stock[key2])
                        customer_sheet[key1] = list1
                        
                    elif key1 in customer_sheet:
                        list2 = []
                        list2.append(key2)
                        list2.append(sellPrice)
                        list2.append(sellPrice - stock[key2])
                        customer_sheet[key1].append(list2)
        print ("each customer can affordable bellow:")
        for key in customer_sheet:
            print ("customerName:" + key + "\n" + str(customer_sheet[key]))
        
        #print (key1,"has affordable to buy:","\n",key2,"\n","price is:",stock[key2] + 0.5 * stock[key2],"\n","seller_profit:",sellPrice - stock[key2])
    global totalProfit
    totalProfit = []
    global selled_bicycles
    selled_bicycles = []
    def purchased_bikes(self,customerName,customerAmount,model):
        self.customerName = customerName
        self.amount = customerAmount
        for key in stock:
            if model == key:
                sellPrice = stock[model] + (0.5 * stock[model])
                profit = sellPrice - stock[model]
                customerBalance = customerAmount - sellPrice
                totalProfit.append(profit)
                selled_bicycles.append(key)
                print ("---------------purchased Inventory---------------------")
                #print ("customer name:" + customerName)
                print('customerName: {}'.format(customerName))
                print ('Customer choosed model: {}'.format(model)) 
                print ('Selled Price: {}'.format(sellPrice))
                print ('Profit they made by selling that model: {}'.format(profit))
                print ('customer still have after purchase: ${}'.format(customerBalance))
                print ('Total weight of {} bicycle: {}lb'.format(model,weight[model]))
        
    def total_profit(self):
        total = 0
        for num in totalProfit:
            total = total + num
        print ("------------------Total Profit After Selling 3 Bicycles-------")
        print ('Total Profit after selling three bikes:${}'.format(total)) 
        
    def remaining_stock(self):
        temp_stock = stock
        for key in list(stock):
            for bike in selled_bicycles:
                if key == bike:
                    del temp_stock[bike]
        print ("-----------------remaining stock------------------"+"\n"+str(temp_stock))
        
    
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
