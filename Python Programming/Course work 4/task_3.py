# Custom exception for negative numbers
class NegativeNumberError(Exception):
    pass

try:
    # Taking user input
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Checking for negative number
    if num1 < 0 or num2 < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")

    # Division operation
    result = num1 / num2

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except NegativeNumberError as e:
    print(f"Error: {e}")

except ValueError:
    print("Error: Please enter valid integers.")

else:
    print(f"Result: {result}")

finally:
    print("Program execution completed.")