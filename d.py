# Bubble Sort v3
# 1. Initialise an unsorted
listL= [5, 7, 3, 6, 2, 4, 1]
print("INPUT (initial list): ", L)
exchange = Truen = len(L)i = 0
# 2. Traverse across every element as long as there are exchanges
while (i< n) and  exchange:
    print("BEFORE PASS %d: %s " %(i+1, L))
    exchange = False
    # assume that there will be no exchanges# 3.Compare all unsorted adjacent elementsfor j in range(n-i-1):# 4. if the elements are out of order, then swap themprint("%s " %L, end="-> ")if L[j] > L[j+1]:L[j], L[j+1] = L[j+1], L[j] # Canonical swap!exchange = True # we've done an exchange!print("%s " %L)print("AFTER PASS %d: %s " %(i+1, L))i= i+1 # increment the loop counterprint("OUTPUT (sorted list): ", L)