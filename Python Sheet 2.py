#Question 1.
n1 = input('Enter a number: ')
n2 = input('Enter another number: ')
if n1 > n2:
    print('Your numbers from largest to smallest are the following:')
    print(n1, 'and', n2)
else:
    print('Your numbers from largest to smallest are the following: ')
    print(n2, 'and', n1)
    
#Question 2.
age = int(input('Please enter your age: '))

if age >= 18:
    print('User is elegible for voting')
else:
    print('Access Denied, You are not elegible to vote')
    
#Question 3.
n = int(input('Enter a number: '))
if n % 2 == 0:
    print('Your numberis even!!!')
else:
    print('Your number is odd!!!')
    
#Question 4.
number = int(input('Enter a number: '))
if number % 7 == 0:
    print('Your number is a factor of 7')
else:
    print('Your number is not a a factor of 7')

#Question 5.
number = int(input('Enter a number: '))
if number % 5 == 0:
    print('Hello')
else:
    print('Bye')
    
#Question 6.
units = int(input('Enter the amount of units of electricity you used: '))
if  units <= 100:
    print('No charge for the amount of units used.')
elif 100 < units >= 200:
    charge5Cents = units * 5
    print('Your amount charged is,', charge5Cents, 'cents')
else:
    charge10Cents = units * 10
    print('Your amount charged is,', charge10Cents, 'cents')
    

#Question 7.
num = int(input('Enter a number: '))
lastDigit = num % 10
print(lastDigit)
    

#Question 8.
num = int(input('Enter a number: '))
lastDigit = num % 10
if lastDigit % 3 == 0:
    print(lastDigit)
    print('This is a factor of 3')
else:
    print(lastDigit)
    print('This is not a factor of 3')
    
#Question 9.
numero = int(input('Enter a number from 1-7 inclusive: '))
if numero == 1:
    print('Sunday')
elif numero == 2:
    print('Monday')
elif numero == 3:
    print('Tuesday')
elif numero == 4:
    print('Wednesday')
elif numero == 5:
    print('Thursday')
elif numero == 6:
    print('Friday')
elif numero == 7:
    print('Saturday')
else:
    print('Not an eligible number')


    
    
    
    
    
    
    
    
    
    
    
    
    
    