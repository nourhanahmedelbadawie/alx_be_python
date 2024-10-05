num1 = int(input('Enter the first number:'))

num2 =int(input('Enter the second number:'))

operation = input('Choose the operation (+, -, *, /):')

result = 0

match operation:
    case '+':
       result = (num1 + num2) # code for pattern 1
    case '-':
        result = (num1 - num2) 
    case '*':
        result = (num1 * num2) # code for pattern 1
    case '/':
       if num2 == 0:
         result = ('You try to divide by zero.')
       else:
         result = (num1 / num2) 
    case _:
        print('Choose the operation')


print('The result is ' , result , '.')