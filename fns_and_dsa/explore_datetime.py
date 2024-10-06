
from datetime import datetime
from datetime import timedelta 
from datetime import date 

def display_current_datetime() :

 current_date =  datetime.now()

 return current_date
current_date = display_current_datetime()

print('current data is ' , current_date)

days = int(input(' enter a number of days'))


def calculate_future_date(days):
 future = date.today()   + timedelta(days=days) 
 return future

future_date =   calculate_future_date(days) 

print('future data is ' , future_date)
