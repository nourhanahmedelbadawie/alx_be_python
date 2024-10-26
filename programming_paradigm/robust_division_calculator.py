def safe_divide(numerator, denominator):
  return  float(numerator)  /  float(denominator)

try:
  numerator = input("Enter numerator:")
  denominator = input("Enter denominator:")
  res = safe_divide( numerator  ,  denominator) 
  
except ZeroDivisionError:
  print("Error: Cannot divide by zero.")
except ValueError :
  print("Error: Cannot divide by non number.")

