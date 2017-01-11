from pandas import Series,DataFrame
import pandas as pd

class bicycle(object):
    
    def __init__(self,modelName,weight,cost):
        self.modelName = modelName
        self.weight = weight
        self.cost = cost
       
    def bicycle_details(self):
        print(self.modelName)
        print(self.weight)
        print(self.cost)
