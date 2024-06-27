import random
import math

lower = int(input('enter the lower bound:'))

upper = int(input('enter the upper bound'))

x= random.randint(lower,upper)

maths = round(math.log(upper - lower + 1,2))

print(f'you have only {maths} try')

count = 0

while True:
    count += 1
    guess = int(input(f'guess a number between {lower} and {upper}:'))
    

    if x == guess:
        print(f'\ncongratualtion you did it in {count} try')
        break
    elif x>guess:
        print('\nyour guess is too low')
    elif x<guess:
        print('\nyour guess is to high')

if count >=math.log(upper-lower+1,2):
    print('\n the number is %d'%x)
    print('\n better luck next time')
