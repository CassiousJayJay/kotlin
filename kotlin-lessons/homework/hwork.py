# Name: ...
# CSE 140
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.
import cmath                  # makes the math.sqrt function available

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

d = (b ** 2) - (4 * a * c)

x1 = (-b - cmath.sqrt(d))/ 2 * a
x2 = (-b + cmath.sqrt(d))/ 2 * a
print("The value of x: ", x1 ,"The value of x: ", x2)


# ... write your code and comments here (and remove this line)


###
### Problem 2
x = int(input("Enter the value of x: "))
y = 1 / x
print("The reciprocal of x: ", y)



print ("Problem 3 solution follows:")

# ... write your code and comments here (and remove this line)


###
### Problem 4
###
num = int(input("Enter the number: "))
factorial = 1

if num == 0:
    print("The factorial of 0 is 1")
elif num < 0:
    print("Negative number does not have a factorial")
else:
    for i in range(1, num + 1):
                factorial = factorial * i
                print("The factorial is: ", factorial)



###
### Problem 5
def factorial(x):
    for i in range(x, 0, -1):
        yield cmath.factorial(i)

results = factorial(10)

for num in results:
    print(num) 

###
### Problem 6
###

print ("Problem 6 solution follows:")

# ... write your code and comments here (and remove this line)


###
### Collaboration
###

# ... Write your answer here, as a comment (on lines starting with "#").


###
### Reflection
###

# ... Write your answer here, as a comment (on lines starting with "#").