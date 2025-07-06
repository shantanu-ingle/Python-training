
import math

def precedence(op):
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    return 0

def apply_operator(num_stack, op_stack):
    op = op_stack.pop()
    if op in ('+', '-', '*', '/'):
        num2 = num_stack.pop()
        num1 = num_stack.pop()
        result = evaluate(num1, num2, op)
        num_stack.append(result)
    else:  # function like sin, cos, tan
        num = num_stack.pop()
        result = evaluate_function(op, num)
        num_stack.append(result)

def evaluate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 // num2

def evaluate_function(func, num):
    if func == 'sin':
        return math.sin(math.radians(num))
    elif func == 'cos':
        return math.cos(math.radians(num))
    elif func == 'tan':
        return math.tan(math.radians(num))
    elif func == 'sqrt':
        return math.sqrt(num)
    elif func == 'log':
        return math.log10(num)
    elif func == 'ln':
        return math.log(num)
    

def evaluate_expression(expression):
    num_stack = []
    op_stack = []
    num = None
    i = 0
    n = len(expression)
    while i < n:
        char = expression[i]
        if char.isdigit():
            num = int(char)
            while i + 1 < n and expression[i + 1].isdigit():
                i += 1
                num = num * 10 + int(expression[i])
            num_stack.append(num)
            num = None
        elif char.isalpha():
            # Parse function name
            func = char
            while i + 1 < n and expression[i + 1].isalpha():
                i += 1
                func += expression[i]
            op_stack.append(func)
        elif char == '(': 
            op_stack.append(char)
        elif char == ')': 
            while op_stack and op_stack[-1] != '(': 
                apply_operator(num_stack, op_stack)
            op_stack.pop()  
         
            if op_stack and op_stack[-1] not in '+-*/(':
                apply_operator(num_stack, op_stack)
        elif char in '+-*/':
            while (op_stack and op_stack[-1] != '(' and
                   precedence(op_stack[-1]) >= precedence(char)):
                apply_operator(num_stack, op_stack)
            op_stack.append(char)
        i += 1
    while op_stack:
        apply_operator(num_stack, op_stack)
    if len(num_stack) != 1:
        raise ValueError("Invalid expression.")
    return num_stack[0]

def main():
    expression = input("Enter the expression: ")
    try:
        result = evaluate_expression(expression)
        print("The result of the expression is:", result)
    except Exception as e:
        print("Error:", e)

main()
