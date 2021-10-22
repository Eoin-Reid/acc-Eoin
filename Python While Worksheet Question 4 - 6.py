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
    hcf = bigN // smallN
    mod = bigN % smallN
    print(bigN, '//', smallN, '=', bigN//smallN, 'Remainder =', mod)
    bigN = smallN
    smallN = mod
    
print('HCF = ', hcf)

#Question. 6
decNum = int(input('Enter a number'))
r = 1
p = 1
output = ''
while p != 0:
    p = decNum // 2
    r = decNum % 2
    print(decNum, '// 2 =', p, 'remainder =', r)
    decNum -= p + r
    output = output + str(r)
print(output)
    
    


