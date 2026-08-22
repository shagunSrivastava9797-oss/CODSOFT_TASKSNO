def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("===== SIMPLE CALCULATOR =====")

    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please select 1-5.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = add(num1, num2)
            symbol = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            symbol = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            symbol = "*"
        elif choice == "4":
            result = divide(num1, num2)
            symbol = "/"

        print(f"\nResult: {num1} {symbol} {num2} = {result}")


if __name__ == "__main__":
    main()
  
  ===== SIMPLE CALCULATOR =====

Select operation:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Exit
Enter choice (1-5): 1
Enter first number: 1
Enter second number: 2

Result: 1.0 + 2.0 = 3.0

Select operation:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Exit
Enter choice (1-5): 3
Enter first number: 4
Enter second number: 5

Result: 4.0 * 5.0 = 20.0

Select operation:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Exit
Enter choice (1-5): 5
Goodbye!
