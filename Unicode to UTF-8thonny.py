file = open('unicode.txt', 'r')
g = file.read()
y = g.replace('U+0x', '\n')
for num in y:
    if num == '0':
        num = '0000'
    elif num == '1':
        num = '0001'
    elif num == '2':
        num = '0010'
    elif num == '3':
        num = '0011'
    elif num == '4':
        num = '0100'
    elif num == '5':
        num = '0101'
    elif num == '6':
        num = '0110'
    elif num == '7':
        num = '0111'
    elif num == '8':
        num = '1000'
    elif num == '9':
        num = '1001'
    elif num == 'A' or num == 'a':
        num = '1010'
    elif num == 'B' or num == 'b':
        num = '1011'
    elif num == 'C' or num == 'c':
        num = '1100'
    elif num == 'D' or num == 'd':
        num = '1101'
    elif num == 'E' or num == 'e':
        num = '1110'
    elif num == 'F' or num == 'f':
        num = '1111'
    print(num, end=' ')
        
file.close()





