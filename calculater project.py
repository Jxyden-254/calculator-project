  
  def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_operation():
    valid_operations = {'+', '-', '*', '/'}
    while True:
        operation = input("Enter operation (+, -, *, /): ")
        if operation in valid_operations:
            return operation
        print("Please enter a valid operation.")

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/' and num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero"

def main():
    print("Simple Calculator")
    print("-----------------")
    
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    operation = get_operation()
    
    result = calculate(num1, num2, operation)
    
    print(f"\n{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()