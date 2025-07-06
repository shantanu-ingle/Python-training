#factorial of a number with recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
    
print(factorial(5))

#time complexity is O(n)
#space complexity is O(n) as it uses stack

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
#space complecity reduced to O(1) as it uses constant space
