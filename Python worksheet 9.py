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
























