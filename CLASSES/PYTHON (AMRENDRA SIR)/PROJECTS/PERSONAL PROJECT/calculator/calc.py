# Python Calculator

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def modulus(a, b):
    return a % b


def floor_divide(a, b):
    return a // b


def calculator():
    print("=" * 35)
    print("        PYTHON CALCULATOR")
    print("=" * 35)

    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Floor Division (//)")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "7":
            print("\nThank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("\nInvalid choice. Please select 1-7.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)

            elif choice == "2":
                result = subtract(num1, num2)

            elif choice == "3":
                result = multiply(num1, num2)

            elif choice == "4":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue
                result = divide(num1, num2)

            elif choice == "5":
                if num2 == 0:
                    print("Error: Cannot find modulus with zero.")
                    continue
                result = modulus(num1, num2)

            elif choice == "6":
                if num2 == 0:
                    print("Error: Cannot perform floor division by zero.")
                    continue
                result = floor_divide(num1, num2)

            print(f"\nResult: {result}")

        except ValueError:
            print("\nError: Please enter valid numbers.")


# Start the calculator
calculator()