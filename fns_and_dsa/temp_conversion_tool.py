FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


temp = float(input('Enter the temperature to convert:'))
type = (input('Is this temperature in Celsius or Fahrenheit? (C/F):'))

def convert_Temp(temp , type):
     if(type == 'F'):  
           print(f"{temp}°F is  {convert_to_fahrenheit(temp)}°C")
     elif (type == 'C'):  
           print(f"{temp}°C is  {convert_to_fahrenheit(temp)}°F")
     else:
          print('Invalid temperature. Please enter a numeric value.')



def convert_to_celsius(fahrenheit):
    return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR



def convert_to_fahrenheit(celsius):
      return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR


convert_Temp(temp , type)
