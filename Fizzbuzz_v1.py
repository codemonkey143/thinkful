# Creating FizBuzz

'''
Rules:
    take number from 1 to 100
    if the number is evenly divisible by 3 say FizzBuzz
    if the number is evenly divisible by 3 then say Fizz
    if the number is evenly divisible by 5 then say Buzz
    Otherwise say the number
'''

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print ('fizz buzz')
    elif num % 3 == 0:
        print ('fizz')
    elif num % 5 == 0:
        print ('buzz')
    else:
        print(num)
