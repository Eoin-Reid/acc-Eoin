import random
import math

a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
lower = 0
upper = 0
if a < b:
    lower = a
    upper = b
else:
    lower = b
    upper = a

rn = random.randint(lower, upper)
guess = 1

count = round(math.log(upper - lower + 1, 2))
print('You maximum number of guesses is, ', count)

while count != 0:
    guess = int(input('Enter a Guess, '))
    if guess == rn:
        print('Congradulations, You WIN!!!')
        print('The random number between', a, 'and', b, 'is', rn)
        print('You had', count, 'number of guesses left!!!')
        count = 0
    elif guess != rn and count > 1:
        count -= 1
        print('Incorrect, Please try again')
        print('You have', count, 'number of guesses left!!!')
        if guess > rn:
            print('Your previous guess was too high')
        else:
            print('Your previous guess was too low')
    else:
        print('Incorrect, You have run out of Guesses')
        count = 0
