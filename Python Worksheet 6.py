#Question 1
for i in range(10):
    print(i)
print('End of q1')

#Question 2
evenN = 0
sumO = evenN
for evenN in range(10, 21, 2):
    print(evenN, '+', sumO, '=', evenN + sumO)
    sumO = evenN + sumO

#Question 3
for num in range(10, 0, -2):
    print(num)
print('End of q3')

#Question 4
for num1 in range(10):
    num1 = num1 * num1
    print(num1)
print('End of q4')

#Question 5/6
d = '*'
user = int(input('Enter the amount of rows you want displayed, '))
for num2 in range(user):
    if num2 == 0:
        print(d)
    elif num2 == 1:
        print(d*2)
    elif num2 == 2:
        print(d*3)
    elif num2 == 3:
        print(d*4)
    else:
        print(d*5)
print('End of q5')

#Question 7
for num3 in range(5):
    variable = int(input('Enter an integer, '))
    print(variable)