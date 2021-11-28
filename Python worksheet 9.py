#Question 1
print('Question 1')
list1 = []
print(list1)

#Question 2
print('Question 2')
list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x = 1
i = 3
j = 10
list2[i] = x
print(list2)

list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list2[i])

list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list2[-i])

list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list2[i:j])

list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list2[i:])

list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
del list2[i]
print(list2)

list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2.append(x)#appends x to the end of the list

list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2.extend([12]) #appends 12 to the end of the list
print(list2)

list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2.insert(6,87) #inserts 87 at 6 position
print(list2)

list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2.remove(9) #removes the first list item whose value is 9
print(list2)

list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
position = list2.pop(14) #removes the item at position 14 and returns its value
print(list2)
print(position)

list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2.clear() #removes all items from the list
print(list2)

list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list2.index(5)) #returns the position of the first occurrence of x in a list

list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list2.count(10)) #returns the number of times x appears in a list

list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2.reverse() #reverses list elements
print(list2)

list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2.copy() #returns a copy of the list
print(list2)

#Question 3
print('Question 3')
 
while True:
    list3 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    print(list3)
    print('''1. Append an element
    2. Insert an element
    3. Append a list to the given list
    4. Modify an existing element
    5. Delete an existing element from its position
    6. Delete an existing element with a given value
    7. Sort the list in the ascending order
    8. Sort the list in descending order
    9. Display the list.''')
    option = int(input('Please enter your choice (1-9): '))
    
    while option == 1:
        us = input('Enter something you want to append, ')
        list3 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        lapp = list3.append(us)#Appendes us to end of list
        print(list3)
        ip = int(input('Enter 1 if you want to reapeat and 0 to return to main menu: '))
        if ip == 1:
            option = 1
        elif ip == 0:
            option = 0
       
    while option == 2:
        place = int(input('Enter where you want exchange it:'))
        list3 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        insrt = int(input('Enter what you want to insert: '))
        inst = list3.insert(place, insrt)#substitutes a character for another using its position
        print(list3)
        ip = int(input('Enter 1 if you want to reapeat and 0 to return to main menu: '))
        if ip == 1:
            option = 2
        elif ip == 0:
            option = 0
    
    while option == 3:
        a = input('Enter a list to append: ')
        list3 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        list3.append(a)#appends a list at the end
        print(list3)
        ip = int(input('Enter 1 if you want to reapeat and 0 to return to main menu: '))
        if ip == 1:
            option = 3
        elif ip == 0:
            option = 0
       
    while option == 4:
        x = int(input('Enter what you want to modify:'))
        insrt = int(input('Enter what you want to modify it to: '))
        list3[x] = insrt#substitutes a character for another using its value
        print(list3)
        ip = int(input('Enter 1 if you want to reapeat and 0 to return to main menu: '))
        if ip == 1:
            option = 4
        elif ip == 0:
            option = 0
        
    while option == 5:
        c = int(input('Enter a charcter to delete: '))
        del list3[c]#Deletes character from position c
        print(list3)
        ip = int(input('Enter 1 if you want to reapeat and 0 to return to main menu: '))
        if ip == 1:
            option = 5
        elif ip == 0:
            option = 0
        
    while option == 6:
        d = int(input('Enter an existing element with a given value to delete: '))
        list3.remove(d)#Delete all characters with value d
        print(list3)
        ip = int(input('Enter 1 if you want to reapeat and 0 to return to main menu: '))
        if ip == 1:
            option = 6
        elif ip == 0:
            option = 0
    
    while option == 7:
        list3.sort()
        print(list3)
        ip = int(input('Enter 1 if you want to reapeat and 0 to return to main menu: '))
        if ip == 1:
            option = 7
        elif ip == 0:
            option = 0
    
    while option == 8:
        list3.sort()
        list3.reverse()
        print(list3)
        ip = int(input('Enter 1 if you want to reapeat and 0 to return to main menu: '))
        if ip == 1:
            option = 8
        elif ip == 0:
            option = 0
        
    while option == 9:
        list3.copy
        print(list3)
        ip = int(input('Enter 1 if you want to reapeat and 0 to return to main menu: '))
        if ip == 1:
            option = 9
        elif ip == 0:
            option = 0
        

        
        
    



