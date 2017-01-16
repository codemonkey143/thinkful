class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()
        
    def fireMusician(self,combust):
        self.combust = combust
        for i in self.combust:
            self.sounds.remove(i)
        print(self.sounds)
        
    def hireMusician(self,combust):
        self.combust = combust
        for i in self.combust:
            self.sounds.append(i)
        print(self.sounds)
    
# The Musician class is the parent of the Bassist class

class Bassist(Musician): 
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Bask","Bow","Tango","Mono"])
        
        
class Brands(Musician):
    def __init__(self):
        #Call the __init__method of the parent class
        super().__init__(["Bask","Task","Capl"])

nigel = Drummer()
nigel.solo(4)
print (nigel.sounds)
print (nigel.fireMusician(["Bow","Tango"]))

nigelq = Brands()
nigelq.solo(3)
print(nigelq.fireMusician(["Capl"]))
print(nigelq.hireMusician(["Mazp","Dupli"]))

