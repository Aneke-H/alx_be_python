FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    """
    # global FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

    return f"{fahrenheit}°F is {(fahrenheit - 32)  * FAHRENHEIT_TO_CELSIUS_FACTOR}°C"

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    """
    # global CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

    return f"{celsius}°C is {celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32}°F"
def main():
    """Entry point of the program"""
    try:
        temperature= float(input("Enter the temperature to convert: "))
        temperature_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        if temperature_unit == 'F':
            return convert_to_celsius(temperature)
        elif temperature_unit == 'C':
            return convert_to_fahrenheit(temperature)
        else:
            print("Invalid convesion, Please try again.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__=="__main__":
    main()
