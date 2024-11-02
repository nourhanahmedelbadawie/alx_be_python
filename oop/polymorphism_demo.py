import math

class Shape:

   def __init__(self , area):
     self.area = area
      

class Rectangle:
      def __init__(self ,  length , width):
        self.area = length * width
      



class Circle:
       def __init__(self ,  radius ):
                  self.area = math.pi * (radius ** 2)