#temperature
def temperature():
  Farhenite = float(input("Enter temperature in farhenite : "))
  celsius = (Farhenite - 32) * 5.0 / 9.0
  print(f"Temperature : {Farhenite}F = {celsius}C")

temperature()