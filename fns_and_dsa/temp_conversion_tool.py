FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{temperature}°F is {celsius}°C")


def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{temperature}°C is {fahrenheit}°F")

while True:
    try:
        temperature = float(input("Enter the temperature to convert: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

while True:
        metric =input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if metric == "F":
            convert_to_celsius(temperature)
            break
        elif metric == "C":
            convert_to_fahrenheit(temperature)
            break
        else:
            print("wrong input")


