import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


#Q :Write a function to ask what style of drink a customer likes

preferences = {}

def customer_preferences(questions):
    for key in questions:
        while True:
            output = raw_input(questions[key]+"Y/N:").lower()
            if output == 'y':
                preferences[key] = 'True'
                break
            elif output == 'n':
                preferences[key] = 'False'
                break
    return preferences
        

#Q :Write a function to construct a drink
def  customized_drink(preferences):
    drink = []
    for key in preferences:
        if preferences[key] == 'True':
            drink.append(ingredients[key])
    print ("Hey customer_preferences drink {}:".format(customized_drink.__name__))
    return random.choice(drink)
    
            
            
if __name__ == '__main__':
    customer_preferences(questions)
    print(customized_drink(preferences))
