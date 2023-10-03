import math

def factorial(x):
    for i in range(x, 0, -1):
        yield math.factorial(i)

results = factorial(10)

for num in results:
    print(num) 