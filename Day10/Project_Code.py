#Calculator
from replit import clear
from art import logo
#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

#Recursive function
def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    for operation in operations:
        print(operation)

    flag = True
    while flag:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        selected_operation = operations[operation_symbol]
        answer = selected_operation(num1 , num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            flag = False
            clear()
            calculator()

calculator()

