import sys

from Fizzbuzz import check_fizzbuzz

try:
    print ("name of the script is {}".format(sys.argv[0]))
    
    print ("user supplied{} arguments at the run time".format(len(sys.argv)))
    
    if len(sys.argv) > 1:
        for argv in sys.argv[1:]:
            check_fizzbuzz(int(argv))
    elif len(sys.argv) == 1:
        argv = int (input("please enter number:"))
        check_fizzbuzz(int(argv))
        
except ValueError:
    print ("please enter numeric value")
