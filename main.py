import os
import platform
import CalcLogo


def clear_terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def plus_op(num1, num2):
    return num1 + num2


def subtraction_op(num1, num2):
    return num1 - num2


def multiplication_op(num1, num2):
    return num1 * num2


def division_op(num1, num2):
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return num1 / num2


operations = {
    '+': plus_op,
    '-': subtraction_op,
    '*': multiplication_op,
    '/': division_op
}


def get_valid_operator():
    while True:
        op = input("Pick An Operator (+, -, *, /): ")
        if op in operations:
            return op
        else:
            print("Invalid operator. Please choose one from the list: +, -, *, /")


def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    result = 0
    while True:
        if result == 0:
            x = get_valid_number("What's The First Number: ")
        else:
            x = result

        op = get_valid_operator()
        y = get_valid_number("What's The Second Number: ")

        result = operations[op](x, y)

        if result is not None:
            print(f"{x} {op} {y} = {result}")

        while True:
            ch = input(
                f"Type 'y' to continue calculation with the {result}, 'n' to start a new calculation, or 'q' to quit: ").strip().lower()
            if ch == 'y':
                clear_terminal()
                print(CalcLogo.logo)
                break
            elif ch == 'n':
                clear_terminal()
                print(CalcLogo.logo)
                result = 0
                break
            elif ch == 'q':
                clear_terminal()
                print("Thank you for using Calculator!")
                return
            else:
                print("Invalid input. Please type 'y', 'n', or 'q'.")


if __name__ == "__main__":
    main()
