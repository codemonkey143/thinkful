from bicycles import bicycle
import settings as st
from pandas import Series, DataFrame
import pandas as pd


class bikeshop(bicycle):
    
   def __init__(self,modelName,inventory,margin,profit):
        self.modelName = modelName  
        self.inventory = inventory
        self.margin = margin
        self.profit = profit
   
   def bicycle_model(self):
        name = self.modelName.lower()
        print (name)
    
   def final_price(self):
       for model in st.stock:
           st.updatedStock[model] = st.stock[model] + 0.5 * st.stock[model]
    
       print ("-------------initial stock price -----------------------")
       print (pd.DataFrame(st.stock.items(),columns=['Model Names','Price']))
       print ("-------------updated stock price------------------------")
       print (pd.DataFrame(st.updatedStock.items(),columns=['Model Name','Price']))
       
