#x = 10
#y = 25

#to take inputs from the user
x = input('Enter the value of x: ')
y = input('Enter the value of y: ')

#create a temporaly variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))