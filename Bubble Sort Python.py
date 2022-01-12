# Bubble Sort v1# 1. Initialise an unsorted list

L= [5, 7, 3, 6, 2]
print("INPUT (initial list): ", L)

# 2. Traverse across every element in the list
for i in range(len(L)):
    # 3. Compare all adjacent elements starting from the beginning
    for j in range(len(L)-1):
        # 4. if the elements are out of order, then swap them
        if L[j] > L[j+1]:
            temp = L[j+1]
            L[j+1] = L[j]
            L[j] = temp
            
print("OUTPUT (sorted list): ", L)

#Bubble Sort v 2
#1. Initialise an unsorted list

aList = [1, 2, 3, 4]
exchange = True
i= 0
2. Traverse across every element as long as there are exchanges
while (i < len(L)) and (exchange== True):
    exchange = False
    # assume that there will be no exchanges
    # 3. Compare all adjacent elements starting from the beginning
    for j in range(len(L)-1):
        # 4. if the elements are out of order, then swap them
        if L[j] > L[j+1]:
            temp = L[j+1]
            L[j+1] = L[j]
            L[j] = temp
    exchange = True
    # we've done an exchange!i = i+1 # increment the loop counter