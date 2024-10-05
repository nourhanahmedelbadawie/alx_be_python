def perform_operation(num1, num2, operation):
    result = 0  # Initialize result
    if(num2 != 0):
     match operation:
        case 'add':
            result = num1 + num2  # Add numbers
        case 'subtract':
            result = num1 - num2  # Subtract numbers
        case 'multiply':
            result = num1 * num2  # Multiply numbers
        case 'divide':
                return  num1 / num2  # Handle division by zero
        case _:
            return 'Error: Invalid operation.'  # Return an error message for invalid operation
    elif num2 == 0:
     result ='Error: You tried to divide by zero.'
 

    return result
