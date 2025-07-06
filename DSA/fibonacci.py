#fibonaccie series
def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

print(fibonacci(5))

for i in range(6):
    print(fibonacci(i), end=' ')

# time complexity is O(2^n) due to the two recursive calls
# space complexity is O(n) due to the recursion stack

#eithout recursion
def fibonaaci_it(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a + b
    return b
print()
print(fibonaaci_it(5))

