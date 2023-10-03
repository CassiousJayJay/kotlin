a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

#semi_perimeter
s = (a + b + c)/2

#area
area = (s*(s - a) * (s - b) * (s- c)) ** 0.5
print(area)
