#feet to inches
def feet_to_inches(feet):
    inches = feet * 12
    return inches
feet = float(input("Enter measurement in feet: "))
inches = feet_to_inches(feet)
print(f"{feet} feet is equal to {inches} inches.")