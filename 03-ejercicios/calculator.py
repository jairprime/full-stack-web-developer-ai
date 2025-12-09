# Basic calculator

def add(number, number2):
    return number + number2

def subtract(number, number2):
    return number - number2

def multiply(number, number2):
    return number * number2

def split(number, number2):
    if number2 == 0:
        print("Error. You cannot divide by zero.")
    return number / number2

def main ():
    try:
        number = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        while True:
            print("\nOperation menu: ")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. split")
            print("5. Exit")
            option = input("Select on option (1-5): ")

            if option == '1':
                result = add(number, number2)
            elif option == "2":
                result = subtract(number, number2)
            elif option == "3":
                result = multiply(number, number2)
            elif option == "4":
                result = split(number, number2)
            elif option == "5":
                print("Exiting the calcutor.")
                break
            else:
                print("Ivalid option.")
                return
            print(f"The result is {result}.")
    except ValueError:
        print("Invalid entry. Please enter valid numbers.")

main()