# import the complex math module
import math
#variables
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

#calculate the discriminant
d = (b ** 2) - (4 * a * c)


#find the two solutions
solution1 = (-b - math.sqrt(d)) / (2 * a)
solution2 = (-b - math.sqrt(d)) / (2 ** a)

print('The solutions are {0} and {1}'.format(solution1,solution2))
