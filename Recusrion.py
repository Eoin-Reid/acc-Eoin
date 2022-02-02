def factorial(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + factorial(l[1:])
l = [1,2,3,4,5,6,7]
print(factorial(l)) 



def factorial(c):
    if c < 10:
        return c % 10
    else:
        return c % 10 + factorial(c // 10)
c = 1235467
print(factorial(c)) 
