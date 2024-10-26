def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Perform division
        result = num / denom
        return f"The result is: {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter valid numeric values."

# Taking user inputs
numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

# Call the function and display the result or error message
message = safe_divide(numerator, denominator)
print(message)
