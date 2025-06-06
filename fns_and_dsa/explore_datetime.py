from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current_date}")

def calculate_future_date():
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days=number_of_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")

# Function calls
display_current_datetime()
calculate_future_date()




