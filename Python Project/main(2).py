# 4.TYPECASTING
name = "Joe"
age = 18
eyes = 2.0
is_student = True

print(type(name))
print(type(age))
print(type(eyes))
print(type(is_student))

#trying to convert float to integer

eyes = int(eyes)

print(eyes)  #note that the decimal place is removed and the float is converted to an integer.

#trying to convert int to str

age = str(age)

print(type(age))  # age is now a string and that means it will lose its properties as an integer.
                  #integer functions won't work on it anymore
                  #adding 1 to this will not show up as 19 instead as 181.
                  #here 1 is also added as a string and has to be put inside "1".
age += "1"
print(age)


#Conveting str to bool

name = bool(name)

print(name)      #this shows true since there is a value for the name.(name = "Joe")
                 #this would've been false if name had no value(name = "")
