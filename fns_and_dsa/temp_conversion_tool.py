FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celcius(fahrenheit):
    temp_in_celcius = (fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {temp_in_celcius}°C")

def convert_to_fahrenheit(celcius):
    temp_in_fahrenheit = celcius * CELSIUS_TO_FAHRENHEIT_FACTOR +32
    print(f"{celcius}°C is {temp_in_fahrenheit}°F")
def main():
    try:
        temperature = float(input("Enter the temperature to convert: ").strip())
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().lower()

        if unit == "c":
            convert_to_fahrenheit(temperature)
        elif unit == "f":
            convert_to_celcius(temperature)
        else:
            print("Invalid unit! Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Enter a valid temperature and unit!")

if __name__ == "__main__":
    main()
