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
