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
print('End of q2')

#Question 3
for num in range(10, 0, -1):
    print(num)
print('End of q3')

#Question 4
for num1 in range(10):
    num1 = num1 * num1
    print(num1)
    num1 = num1 * num1
    print(num1)
print('End of q4')

#Question 5/6
d = '*'
user = int(input('Enter the amount of rows you want displayed, '))
for num1 in range(user):
    for num2 in range(num1):
        print('*', end = '')
    print('')

#Question 7
variable = 1
for num3 in range(5):
    variable2 = int(input('Enter an integer, '))
    variable = variable * variable2
    print(variable)
    
    