
print("Resource opened successfully")

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: ")) # enter t is wrong for int
    result = a / b
    print(result)
except ZeroDivisionError as zde:
    print("An error occurred: Division by zero is not allowed.", zde)
except ValueError as ve:
    print("An error ocurred: Invalid input, Please enter numeric values only.", ve)
except Exception as e:
    print("An unexpected error occurred", e)

finally:
    print("Resource closed.")

# try block must have either of these
# except / finally / except + finally

print("End of execution")