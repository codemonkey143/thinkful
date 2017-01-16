from bicycles import bicycle

class bicyclemodel(bicycle):
    
    def __init__(self,customerName,model,year,cost):
        self.customerName = customerName
        super(bicyclemodel,self).__init__(model,year,cost)
        
        
bicycle1 = bicyclemodel("daniel","hiking",2015,2000)

customerDetails = bicycle1.__dict__

print (customerDetails)