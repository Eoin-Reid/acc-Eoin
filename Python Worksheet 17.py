import random
print('Hello world')

name = input('Enter name: ')
if name == 'Bob':
    print('Greetings, Bob')
elif name == 'Alice':
    print('Greetings, Alice')
    
n = int(input('Enter a number: '))
counter = 0
for i in range(0, n + 1, 1):
    if i % 5 == 0 or i % 3 == 0:
        counter += i

print(counter)
    
num = int(input('Enter a number: '))
count = 1
count1 = 0
c = input('Enter Operation, Sum or Product: ')
for i in range(1, num + 1, 1):
    if c == 'Product':
        count = count*i
        print(count)
    else:
        count1 += i
        print(count1)
    
for g in range(0, 13, 1):
    for n in range(0, 13, 1):
        a = g * n
        print(g, '*', n, '=', a)

for y in range(2, 51):
    if y > 1:
        for i in range(2, y):
            if y % i == 0:
                break
        else:
            print(y)

answer = random.randint(0, 10)
count = 5
guess = int(input('Enter a guess: '))

while guess != answer and count > 0:

    count -= 1
    if guess > answer:
        print('Your number was too big, Try again')
    else:
        print('Your number was too small, Try again')
    guess = int(input('Enter a guess: '))
    if guess == answer:
        print('You got it!!!')
    if count == 0:
        print('You ran out of guesses')
        
        

x = 2020 + (20 * 4)       
for i in range(2020, x, 4):
    print(i)
        

        
