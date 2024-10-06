
from datetime import datetime
from datetime import timedelta 
from datetime import date 

def display_current_datetime() :

 current_date =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")

 return current_date
current_date = display_current_datetime()

print('current data is ' , current_date)

days = int(input('"Enter the number of days to add to the current date:'))


def calculate_future_date(days):
 future = date.today()   + timedelta(days=days) 
 return future

future_date =   calculate_future_date(days) 

print('future data is ' , future_date.strftime('%Y-%m-%d'))
