# 5.USER INPUT
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(name)

# Input is used when user input is required in a program. In this user input for name is asked first and then it is printed.

print(f"Hello {name}!")
print(f"Hello {name} you are {age} years old!")



# 6.IF STATEMENTS
age = int(input("Enter your age: "))
has_ticket = False
price = 10.00

if age >= 18:
    print("You are an adult.")
    print(f"The ticket price for an adult is ${price}")
elif age < 0:
    print("You are not born yet.")
elif age == 0:
    print("You are a newborn.")
elif age >= 60:
    print("You are a senior citizen.")     #this shows "You are an adult."since if statements come before elif.
else:
    print("You are a child.")
    print(f"The ticket price for a child is ${price * 0.5}")



# 7.LOGICAL OPERATORS
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:        #while using "if" operation if any of statements are satisfied the result is rendered.
    print("Event is cancelled.")
else:
    print("Event is not cancelled.")

is_sunny = True

if temp >= 28 and is_sunny:                    #while using "and" operation all statements have to be true.
    print("It is hot outside.")
    print("It is sunny.")
else:
    print("the weather is good")

if temp >= 28 and not is_sunny:               # "and not" is used when one stament is true and other is not.
    print("It's HOT.")

