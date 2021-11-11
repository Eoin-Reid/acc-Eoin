str1 = input('Enter a sentence,')

strLen = len(str1)
print('Length of sentence =',strLen)

firstc = str1[0]
print('First character of sentence =', firstc)

fthC = str1[4]
print('Fifth character =', fthC)

lC = str1[strLen - 1]
print('Last character =', lC)

for ch in str1:
    print(ch)

for ch in range(0,strLen):
    print(str1[ch])

for ch in range(0,strLen):
    print(ch)