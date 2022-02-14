# print('Hello world')
# 
# name = input('Enter name: ')
# if name == 'Bob':
#     print('Greetings, Bob')
# elif name == 'Alice':
#     print('Greetings, Alice')
#     
# n = int(input('Enter a number: '))
# counter = 0
# for i in range(0, n + 1, 1):
#     if i % 5 == 0 or i % 3 == 0:
#         counter += i
# 
# print(counter)
#     
# num = int(input('Enter a number: '))
# count = 1
# count1 = 0
# c = input('Enter Operation, Sum or Product: ')
# for i in range(1, num + 1, 1):
#     if c == 'Product':
#         count = count*i
#         print(count)
#     else:
#         count1 += i
#         print(count1)
#     
# for g in range(0, 13, 1):
#     for n in range(0, 13, 1):
#         a = g * n
#         print(g, '*', n, '=', a)
for y in range (2, 100, 1):
    for i in range(2, 100, 1):
        if y != i or y != 1:
            if i% y == 0:
                print(i, '%', y, '=', i%y)
        
x = 2020 + (20 * 4)       
for i in range(2020, x, 4):
    print(i)
        
        

        
