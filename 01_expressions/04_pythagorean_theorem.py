#base hypotenus & perpendicular
import math

# Get user input for sides AB and AC
def main():
  ab = float(input("Enter the length of AB: "))
  ac = float(input("Enter the length of AC: "))
  bc = math.sqrt(ab**2 + ac**2)
  print(f"The length of BC (the hypotenuse) is: {bc}")
if __name__ == '__main__':
    main()