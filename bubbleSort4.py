def bubbleSort(L, boolean, debug):
    
    file = open('log.txt', 'w')#Bubble Sort v3
    # 1. Initialise an unsorted
    #L= [5, 7, 3, 6, 2, 4, 1]
    file.write("\nINPUT (initial list): " + str(L))
    exchange = True
    n = len(L)
    i = 0

    file.write(str(L))

    # 2. Traverse across every element as long as there are exchanges
    while (i< n) and  exchange:
        file.write("\nBEFORE PASS: " + str(i + 1) + str(L))
        exchange = False
        # assume that there will be no exchanges
        # 3. Compare all unsorted adjacent elements
        for j in range(n-i-1):
            # 4. if the elements are out of order, then swap them
            file.write("\n " + str(L) + "-> ")
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
            file.write("\n " + str(L))
        file.write("\nAFTER PASS: " +str(i+1) + str(L))
        i= i+1
    file.write('\n' + str(L))

    file.close()
q =  [6, 7, 5, 4, 3, 2, 1]    
bubbleSort(q, True, True)