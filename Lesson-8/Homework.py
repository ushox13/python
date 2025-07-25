try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"The result is: {result}")


except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter a valid integer.")


try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)


except FileNotFoundError:
    print("Error: The file does not exist.")
except TypeError:
    print("Error: Please enter valid numerical inputs.")


try:
    with open("example.txt", "w") as file:
        file.write("This is a test.")


except PermissionError:
    print("Error: You do not have permission to write to this file.")


try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")


except IndexError:
    print("Error: Index out of range.")
except KeyboardInterrupt:
    print("\nInput cancelled by user.")


try:
    with open("example.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)


except UnicodeDecodeError:
    print("Error: There was an encoding issue while reading the file.")


try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)


except AttributeError:
    print("Error: The list does not have the specified attribute.")


try:
    with open("example.txt", "a") as file:
        file.write("\nAppending this text to the file.")
        print("Text appended successfully.")


except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You do not have permission to write to this file.")
