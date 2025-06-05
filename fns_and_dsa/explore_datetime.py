from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    date_and_time = datetime.now()
    current_date = date_and_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date: {current_date}")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    calculated_date = datetime.now() + timedelta(days=number_of_days)
    future_date = calculated_date.strftime("%Y-%m-%d")
    print (f"Future date: {future_date}")

display_current_datetime()
calculate_future_date()