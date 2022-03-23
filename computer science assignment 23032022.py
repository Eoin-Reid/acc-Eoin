inp = input('Enter file name: ')
def readfile():
    
    file = open(str(inp), 'r')
    f = file
    x = len(f.readlines())
    print('Lines = ', x)
     
def read():
    file = open(str(inp), 'r')
    y = len(file.read())
    print('Character = ', y)

def word():
    file = open(str(inp), 'r')
    data = file.read()
    s = len(data.split())
    print('Words = ', s)
    
    

readfile()
read()
word()