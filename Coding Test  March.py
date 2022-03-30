import math

#Question 1
print('Question 1')
n1 = 2.8
n2 = 3.4

mean = (n1 + n2)//2

raD1 = n1 % n2

raD2 = n2 % n1

po = n1 ** n2

print('1) Average =', mean)

print('2) Remainder after Division =', raD1)

print('3) Remainder after Division =', raD2)

print('4)', n1, 'to the power of', n2, '=', po)

#Question 2
print('Question 2')
def Volume(h, r):
    v = math.pi * r**2 * h
    return (v)
h = int(input('Enter height :'))
r = int(input('Enter radius :'))    
print(Volume(h, r))

#Question 3
print('Question 3')

def str_comp(s1, s2):
    if s1 == s2:
        return (True)
    else:
        return (False)

s1 = str(input('Enter a string :'))
s2 = str(input('Enter a string :'))

print(str_comp(s1, s2))

#Question 4

o = int(input('Enter a number :'))
for i in range(1, o):
    if i % 2 != 0:
        print(i)
        
#Question 5
file = open('readme.txt', 'r')
l = file.read()
count = 0
for i in l:
    if i == 'a' or i == 'o'or i == 'u'or i == 'i'or i == 'e' or i == 'A' or i == 'O'or i == 'U'or i == 'I'or i == 'E':
        count += 1
print(count)

#Question 6
def recursive():
    coun1 = 0
    for i in range(1, 5-1):
        coun1 += i
    print(coun1)
    
recursive()
    
file.close()