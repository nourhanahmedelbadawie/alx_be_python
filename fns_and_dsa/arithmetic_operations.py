def perform_operation(num1, num2 , operation):
  result = 0
  match operation:
    case 'add':
       result = (num1 + num2) # code for pattern 1
    case 'subtract':
        result = (num1 - num2) 
    case 'multiply':
        result = (num1 * num2) # code for pattern 1
    case 'divide':
       if num2 == 0:
         result = ('You try to divide by zero.')
       else:
         result = (num1 / num2) 
    case _:
        print('Choose the operation')

  return result