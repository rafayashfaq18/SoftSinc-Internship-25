def calculator():
    print("Simple Calculator")
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        b = float(input("Enter second number: "))
        if op == '+':
            print("Result:", a + b)
        elif op == '-':
            print("Result:", a - b)
        elif op == '*':
            print("Result:", a * b)
        elif op == '/':
            if b != 0:
                print("Result:", a / b)
            else:
                print("Error: Cannot divide by zero.")
        else:
            print("Invalid operation.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    calculator()