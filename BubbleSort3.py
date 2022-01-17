
def bubbleSort(L):
    
    boolean = input('Enter a boolean: ')
    file = open('BubbleSort1.py', 'w')#Bubble Sort v3
    # 1. Initialise an unsorted
    #L= [5, 7, 3, 6, 2, 4, 1]
    print("INPUT (initial list): ", L)
    exchange = True
    n = len(L)
    i = 0

    file.write(str(L))

    # 2. Traverse across every element as long as there are exchanges
    while (i< n) and  exchange:
        print("BEFORE PASS %d: %s " %(i+1, L))
        exchange = False
        # assume that there will be no exchanges
        # 3. Compare all unsorted adjacent elements
        for j in range(n-i-1):
            # 4. if the elements are out of order, then swap them
            print("%s " %L, end="-> ")
            if boolean == True:
                if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
                    # Canonical swap!
                    exchange = True
                    # we've done an exchange!
            else:
                if L[j] < L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
                    # Canonical swap!
                    exchange = True
                    # we've done an exchange!
            print("%s " %L)
        print("AFTER PASS %d: %s " %(i+1, L))
        i= i+1
    file.write('\n' + str(L))

    file.close()
q = [2,1,3]    
bubbleSort(q)
