variable = input('Enter 1 for Insertion Sort or 2 for Bubble Sort: ')
if variable == '1':
    def InsertionSort(L, b = False):
        # 1. Initialise an unsorted list
        # 2. Initialise a marker​
        marker = 1
        # 3. Traverse through all list items​

        while (marker < len(L)):

            # 4. Insert the selected item to its correct position​

            j = marker

            if b == True:
                while (L[j] < L[j-1] and j>0):
                    tmp = L[j]

                    L[j] = L[j-1]

                    L[j-1] = tmp

                    j = j - 1

                    # 6. Advance the marker to the right by 1 position

                marker = marker+1
                print(L)
                    
            elif b == False:
                while (L[j] > L[j-1] and j>0):
                    tmp = L[j]

                    L[j] = L[j-1]

                    L[j-1] = tmp

                    j = j - 1

                    # 6. Advance the marker to the right by 1 position

                marker = marker+1
                print(L)
    q = [6, 7, 5, 4, 3, 2, 1] 
                
    InsertionSort(q, False)


elif variable == '2':
    def bubbleSort(L, boolean = False):
        # 1. Initialise an unsorted
        #L= [5, 7, 3, 6, 2, 4, 1]
        print("INPUT (initial list): " , L)
        exchange = True
        n = len(L)
        i = 0

        print(L)

        # 2. Traverse across every element as long as there are exchanges
        while (i< n) and  exchange:
            print("BEFORE PASS: " , (i + 1) , L)
            exchange = False
            # assume that there will be no exchanges
            # 3. Compare all unsorted adjacent elements
            for j in range(n-i-1):
                # 4. if the elements are out of order, then swap them
                print(L , '->' )
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
                print(L)
            print("AFTER PASS: ", (i+1),  str(L))
            i= i+1
        print(L)

    q =  [6, 7, 5, 4, 3, 2, 1]    
    bubbleSort(q, False)
        
