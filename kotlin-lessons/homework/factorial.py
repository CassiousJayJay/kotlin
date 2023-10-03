results = int(input("Enter the number: "))
factorial = 1
for i in range(1, 10):
    factorial = factorial * i
    results.append(int('{:2,}! = {:,}'.format(i, factorial)))
    print('\n'.join(reversed(results)))