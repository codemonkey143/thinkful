from bikeshops import bikeshop
from bicycles import bicycle
import settings as sc
#import pandas as pd

class customer(object):
    
    def __init__(self,name,fund,newbicycle):
        self.name = name
        self.fund = fund
        self.newbicycle = newbicycle
        
    def customer_inventory(self):
        for key1 in sc.customers:
            for key2 in sc.stock:
                if sc.customers[key1] >= sc.stock[key2]:
                    sellPrice = sc.stock[key2] + 0.5 * sc.stock[key2]
                    if key1 not in sc.customer_sheet:
                        global list1 
                        list1 = []
                        list1.append(key2)
                        list1.append(sc.stock[key2] + 0.5 * sc.stock[key2])
                        list1.append(sellPrice - sc.stock[key2])
                        sc.customer_sheet[key1] = list1
                        
                    elif key1 in sc.customer_sheet:
                        list2 = []
                        list2.append(key2)
                        list2.append(sellPrice)
                        list2.append(sellPrice - sc.stock[key2])
                        sc.customer_sheet[key1].append(list2)
        print ("each customer can affordable bellow:")
        #print (pd.DataFrame(sc.customer_sheet.items()))
        print(sc.customer_sheet)
        #print (key1,"has affordable to buy:","\n",key2,"\n","price is:",stock[key2] + 0.5 * stock[key2],"\n","seller_profit:",sellPrice - stock[key2])
    
    def purchased_bikes(self,customerName,customerAmount,model):
        self.customerName = customerName
        self.amount = customerAmount
        for key in sc.stock:
            if model == key:
                sellPrice = sc.stock[model] + (0.5 * sc.stock[model])
                profit = sellPrice - sc.stock[model]
                customerBalance = customerAmount - sellPrice
                sc.totalProfit.append(profit)
                sc.selled_bicycles.append(key)
                print ("---------------purchased Inventory---------------------")
               
                print('customerName: {}'.format(customerName))
                print ('Customer choosed model: {}'.format(model)) 
                print ('Selled Price: {}'.format(sellPrice))
                print ('Profit they made by selling that model: {}'.format(profit))
                print ('customer still have after purchase: ${}'.format(customerBalance))
                print ('Total weight of {} bicycle: {}lb'.format(model,sc.weight[model]))
        
    def total_profit(self):
        total = 0
        for num in sc.totalProfit:
            total = total + num
        print ("------------------Total Profit After Selling 3 Bicycles-------")
        print ('Total Profit after selling three bikes:${}'.format(total)) 
        
    def remaining_stock(self):
        temp_stock = sc.stock
        for key in list(sc.stock):
            for bike in sc.selled_bicycles:
                if key == bike:
                    del temp_stock[bike]
                    
        print ("-----------------remaining stock------------------")
        
        #print(pd.DataFrame(temp_stock.items(),columns=['bicycle model','price']))
        #print (temp_stock)
        print ("BicycleModelName        Price")
        for i in temp_stock:
            print ("{}     {}".format(i,temp_stock[i]))