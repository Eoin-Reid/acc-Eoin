str1 = input('Enter a sentence,')

strLen = len(str1)
# print('Length of sentence =',strLen)
# 
firstc = str1[0]
# print('First character of sentence =', firstc)
# 
# fthC = str1[4]
# print('Fifth character =', fthC)
# 
lC = str1[strLen - 1]
# print('Last character =', lC)
# 
# for ch in str1:
#     print(ch)
# 
# for ch in range(0,strLen):
#     print(str1[ch])
# 
# for ch in range(0,strLen):
#     print(ch)
#     
# u = str1.upper()# returns uppercase string
# print(u)
# 
# l = str1.lower() #returns lowercase string
# print(l)
# 
# c = str1.count('x') #counts how many times x appears
# print(c)
# 
# f = str1.find('x') #position of the first occurrence of x
# print(f)
# 
# r = str1.replace('x','y')# replaces x with y
# print(r)
# 
# isL = str1.islower() #returns True if all characters are lowercase
# print(isL)
# 
# isU = str1.isupper() #returns True if all characters are uppercase
# print(isU)
# 
# isNL = str1.isalnum() #returns True if all characters are alphanumeric
# print(isNL)
# 
# isL = str1.isalpha() #returns True if all characters are alphabetic
# print(isL)
# 
# isN = str1.isdigit() #returns True if all characters are digits
# print(isN)
# 
# s = str1.index('s') #returns index of substring s in string
# print(s)
# 
# x = str1.strip('x') #returns a string with leading and trailing characters removed
# print(x)
# 
# #str1[0] = 'W'

str1 = str1.upper()
strLen = len(str1)
strLen2 = int(strLen/2)

result = 1
x = 0
y = len(str1)-1
left  = str1[x]
right = str1[y]

for count in range(strLen2):
    if count < strLen-1:
        print(left, ", ", right)
        x+=1
        y-=1
        if right == left:
            left = str1[x]
            right = str1[y]      
        else:
            result = 0

if result == 1:
    print('It\'s a palindrome')
else:
    print('Not palindrome')






