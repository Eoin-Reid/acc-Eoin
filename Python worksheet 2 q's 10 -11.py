#Question 10.
c = float(input('Enter Degrees Celsius: '))

f = 9/5 * c + 32

roundedF = round(f,2)
          
print('Your degrees in fahrenheit is', roundedF)

dd = int(input('Enter the day of the week: '))
mm = int(input('Enter the month of the year: '))
y = int(input('Enter last 2 digits of the year: '))
c = int(input('Enter first 2 digits of the year: '))

w = ((dd + (13*(mm + 1)//5) + (y//4)+ (c//4) - 2*c) % 7)


print('The day of the week is', w)