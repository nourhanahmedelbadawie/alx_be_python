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
        return "Error: Please enter numeric values only."

# Simulate inputs for testing (or use hardcoded values in non-interactive environments)
try:
    numerator = input()  # No prompt message, assuming automated input
    denominator = input()  # No prompt message, assuming automated input

    # Call the function and print the result or error message
    message = safe_divide(numerator, denominator)
    print(message)

except EOFError:
    # In case of EOFError, print nothing to match expected output format
    pass
