from datetime import datetime
from datetime import timedelta


def display_current_datetime():
    """A function to output the current time and comput a future time
    pased on the number of days inputed by the user."""

    current_date = datetime.now()
    print(f"Current date and time: {current_date}")

    number_of_days= int(input("Enter the number of days to add to the current date: "))
    calculate_future_date = current_date + timedelta(number_of_days)
    return f"Future date: {calculate_future_date.strftime("%Y-%m-%d %H:%M:%S")}"

display_current_datetime()
