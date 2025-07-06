num = 4

# write a function that takes n as input as start from 0 n times to 1 n times in binary. like if n = 3 it should start from 000 to 111 in binary without using and library function
#using recursion form a binary tree of height n and print all the binary numbers from 0 to 2^n - 1
def binaryPattern(n):
    def generateBinary(current, n):
        if len(current) == n:
            print(current)
            return
        generateBinary(current + '0', n)
        generateBinary(current + '1', n)

    generateBinary('', n)

binaryPattern(num)

#any other approach for this without converting to binary
def binaryPatternIterative(n):
    for i in range(2 ** n):
        binary_number = ''
        for j in range(n - 1, -1, -1):
            if i & (1 << j):
                binary_number += '1'
            else:
                binary_number += '0'
        print(binary_number)  

#explain this code