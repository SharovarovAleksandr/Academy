import logging


logging.basicConfig(filename='calcul_lg.log',level=logging.INFO, filemode='w', datefmt='%d-%b-%y %H:%M:%S', format='%(name)s -%(asctime)s -  %(message)s')
lg=logging.getLogger(name='Calculator')

def add(x, y):

    lg.info(f'Execute function adds {x} {y} result {x+y}')
    return x + y

def subtract(x, y):
    lg.info(f'Execute function subtract {x} {y} result {x-y}')
    return x - y

def multiply(x, y):
    lg.info(f'Execute function multiply {x} {y} result {x*y}')
    return x * y

def divide(x, y):
    lg.info(f'Execute function divide {x} {y} result {x/y}')
    return x / y

lg.info('Calculator started !')
while True:
    choice = input("Enter operation choice(+-*/): ")
    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_calculation = input("Let's do next calculation? (y/n): ")
        if next_calculation == "n":
            lg.info('Calculator ended !')
            break
    else:
        print("Invalid Input")
        lg.info('Invalid Input')