import datetime

def display_current_datetime():
    """A function to output the current time and comput a future time
    pased on the number of days inputed by the user."""
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date}")
    number_of_days= int(input("Enter the number of days to add to the current date: "))

    future_date = current_date + datetime.timedelta(number_of_days)
    print(f"Future date: {future_date.date()}")

display_current_datetime()
