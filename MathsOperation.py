# MathsOperation.py

def main():
    # Ask the user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask the user to input a mathematical operation
    operation = input("Enter a mathematical operation (+, -, *, /): ")

    # Perform the operation and display the result
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation!"

    print("The result is:", result)

if __name__ == "__main__":
    main()