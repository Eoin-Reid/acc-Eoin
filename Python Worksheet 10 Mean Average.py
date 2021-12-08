file1 = open('C:/Users/eoing/Downloads/10Random.txt', 'r')
list1 = []
nums = 0
count = 0

for line in file1:
    print(line)
    for numbers in line.strip().split(' '):
        list1.append(int(numbers))
        nums += int(numbers)
        count += 1
mean = nums/count
print('Average =', mean)

file1 = open('C:/Users/eoing/Downloads/100Random.txt', 'r')
list1 = []
nums = 0
count = 0

for line in file1:
    print(line)
    for numbers in line.strip().split(' '):
        list1.append(int(numbers))
        nums += int(numbers)
        count += 1
mean = nums/count
print('Average =', mean)

