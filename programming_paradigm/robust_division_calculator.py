def safe_divide(numerator, denominator):
  return  numerator / denominator

try:
  numerator = input("Enter numerator:")
  denominator = input("Enter denominator:")
  res = safe_divide( numerator  ,  denominator) 
  
except ZeroDivisionError:
  print("Error ZeroDivisionError")
except ValueError :
  print("Error ValueError ")

