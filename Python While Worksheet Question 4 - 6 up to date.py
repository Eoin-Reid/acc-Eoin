#Question. 4
origNum = int(input('Enter a number, '))
count = origNum
factorial = 1
while count > 0:
    factorial = factorial * count
    print('factorial =', factorial)
    count -= 1
    print('Count =', count)
print('The factorial of the number', origNum, ' =', factorial)

#Question. 5
num1 = int(input('Enter a number, '))
num2 = int(input('Enter a number, '))
bigN = 0
smallN = 0

if num1 > num2:
    bigN = num1
    smallN = num2
else:
    bigN = num2
    smallN = num1
    
mod = 1 
while mod != 0:
    mod = bigN % smallN
    print(bigN, '//', smallN, '=', bigN//smallN, 'Remainder =', mod)
    if mod == 0:
        print('Highest Common Factor is', smallN)

    bigN = smallN
    smallN = mod


