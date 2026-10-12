def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

n1 = float(input("Enter first number: "))

keep_going = True
while keep_going:
    operator = input('Choose an operator (+, -, *, /)')
    n2 = float(input("Enter second number: "))
    
    if operator == '+':
        result = add(n1,n2)
    elif operator == '-':
        result = subtract(n1,n2)
    elif operator == '*':
        result = multiply(n1,n2)
    elif operator == '/':
        result = divide(n1,n2)
    else:
        print("Invalid operator!!!")
        


    print(f'{n1} {operator} {n2} = {result}')

choice= input("Type 'y' to continue, 'n' to start over, q to quit: ")
if choice.lower() == 'y':
    n1 = result
elif choice.lower() == 'n':
    n1 = float(input("Enter first number: "))
elif choice.lower() == 'q':
    keep_going = False
    


