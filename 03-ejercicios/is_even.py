# Program is even

try:
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is not even.")
except ValueError:
    print("Error. Ivalid input.")