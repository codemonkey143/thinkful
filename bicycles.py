#from pandas import Series,DataFrame
#import pandas as pd

class bicycle(object):
    
    #unlimited method you can add any number variables you want to use
    def __init__(self,modelName,weight,cost):
        self.modelName = modelName
        self.weight = weight
        self.cost = cost
       
    def bicycle_details(self):
        print(self.modelName)
        print(self.weight)
        print(self.cost)
