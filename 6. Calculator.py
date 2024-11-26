#12. CALCULATOR

num1 = float(input("Enter number 1: "))

operator = input("Enter an operator (+,-,*,/): ")

num2 = float(input("Enter number 2: "))

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
else:
    print(f"{operator} is not a valid operator.")


#13. Weight Conversion
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K" or unit == "k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {weight:.2f} {unit}")
elif unit == "L" or unit == "l":
    weight = weight / 2.205
    unit = "Kg"
    print(f"Your weight is: {weight:.2f} {unit}")
else:
    print(f"{unit} was not valid")

