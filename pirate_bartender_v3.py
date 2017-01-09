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

preferences = {}
drink = []
customer_names = {}

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
        
def  customer_receipe(preferences):
    for key in preferences:
        if preferences[key] == 'True':
            drink.append(ingredients[key])
    name = raw_input("May I know your name:").lower()
    customer_names[name] = random.choice(drink)
    print (customer_names)
    print ("Hey {}:".format(customer_receipe.__name__))
    print (customer_names[name])

if __name__ == '__main__':
    customer_preferences(questions)
    customer_receipe(preferences)
    while True:
        acceptance = raw_input("do you want another drink YES/NO:").lower()
        if acceptance == 'yes':
            while True:
                receipe = raw_input("do you want to try different receipe YES/NO:").lower()
                if receipe == 'yes':
                    name = raw_input("May I know your name:").lower()
                    customer_preferences(questions)
                    customer_names[name] = customer_receipe(preferences)
                elif receipe == 'no':
                    receipe = raw_input("may I know you name:").lower()
                    for key in customer_names:
                        if key == receipe:
                            print (customer_names[key])
                            #customer_receipe(preferences)
                    break
        elif acceptance == 'no':
            break
