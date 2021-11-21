print('Question 1')
str1 = '''Python
programming
is
great
Fun'''
print(str1)

#Question 2
print('Question 2')
usersInput = input('Enter a code using letters and numbers: ')
sum1 = 0
for count in usersInput:
    if count.isdigit():
        sum1 += int(count)
        print(sum1)
        
#Question 3
sen = input('Enter a sentence, ')
print('Question 3')
sen = sen.replace((' '), '-')
print(sen)

#Question 4
print('Question 4')
str2 = str(input('Enter a sentnce, '))
length = len(str2) - 1
count = 0

while count <= length:
    ch = str2[count]
    if ch =='a' or ch=='e' or ch == 'i' or ch == 'o' or ch == 'u':
        print(ch)
    count += 1
    
#Question 5
print('Question 5')
str2 = str(input('Enter a sentnce, '))
length = len(str2) - 1
count = 0

while count <= length:
    ch = str2[count]
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count += 1
    else:
        print(ch)
        count += 1
