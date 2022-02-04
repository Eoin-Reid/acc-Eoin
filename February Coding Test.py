L = [23,1,0,-12,48, 15, 9, 20, -11, 42,7, -5, 13]
#Q.1
counter = 0
for i in L:
    counter += i
    
print('Question 1:', counter)

#Q.2
count = 0
for i in L:
    count = count * i
    
print('Question 2:', count)

# #Q.3
# for i in range(0, 10001, 1):
#     print(i)
#     
#Q.4
s = 'Code Happy'
x = 0
for i in range(0, 10, 1):
    print(s[x])
    x += 1
    
#Q.5
l = int(input('Enter length of rectangle: '))
w = int(input('Enter width of rectangle: '))
a = l * w
print('Question 5: Area =', a)

# #Q.6
character = input('Enter a letter1: ')

while character != 'Z' and character != 'z':
    character = input('Enter a letter: ')
   
        
    
#Q.7
file = open('CS04022022.txt', 'w')
file.write('Leunig -How To Get There\n\nGo to the end of the path until you get to the gate.\nGo through the gate and head straight out towards the horizon.\nKeep going towards the horizon.\nSit down and have a rest every now and again,\nBut keep on going, just keep on with it.\nKeep on going as far as you can.\nThat is how you get there.')
file.close()
    
    
    
    
    
    