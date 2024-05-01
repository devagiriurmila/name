def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
  
    if operation == '+':
        print("Result:", num1 + num2)
    elif operation == '-':
        print("Result:", num1 - num2)
    elif operation == '*':
        print("Result:", num1 * num2)
    elif operation == '/':
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            print("Result:", num1 / num2)
    else:
        print("Invalid operation")

if __name__ == "__main__":
    calculator()
