# checks the fizzbuzz based on the number we provided
def check_fizzbuzz(argv):
    if argv % 3 == 0 and argv % 5 == 0:
        print ('fizz buzz')
    elif argv % 3 == 0:
        print ('fizz')
    elif argv % 5 == 0:
        print ('buzz')
    else:
        print(argv)
