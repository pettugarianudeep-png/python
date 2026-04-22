unit = input ("is this temperature in celsius or Fahrenheit (C?F):")
temp = float(input("Enter the temperature:"))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Farenheit is: {temp}F")
elif unit == "F":
    pass
else:
    print(f"{unit}is an invalid unit of measurement")