# 11.LISTS, TUPLES, SETS

# List [] = mutable(changeable), most flexible
# Tuple () = immutable(unchanging), faster
# Set {} = mutable (add/remove), unordered,     NO duplicates, best for membership testing
# Dictionary {} =


# LIST []

fruits = ["apple", "orange", "banana","coconut"]

print(fruits)                  #this prints all elements in fruits.

for fruit in fruits:           #this prints all elements one by one.
    print(fruit)

fruits[0] = "pineapple"        #this changed the first element(number-0) to pineapple.

for fruit in fruits:
    print (fruit, end=" ")     #this left a space after each fruit.

fruits.append("mango")         #APPEND adds mango to the list
fruits.remove("banana")        #REMOVE removes banana from the list
fruits.pop(0)                  #removes the 1st element in list.
fruits.clear()                 #CLEARs the list and print empty list []

print(fruits)



# TUPLES ()    #CANT BE CHANGED IN ANY WAY

#fruit = ("apple", "orange", "banana","coconut")

#fruits.append("mango")        #not possible
#fruits.remove("apple")        #not possible



# SETS {}      #CAN ADD/REMOVE ELEMENTS BUT CANT CHANGE EXISTING ELEMENTS
               #Unordered and so elements change position everytime.
               #This also means that functions using integers won't work.
               #No Duplicates allowed.

vegetables = {"apple", "orange", "banana","coconut"}
#fruits.append("mango")         #not possible
#fruits[0] = "pineapple"        #not possible

vegetables.add("mango")             #adds mango to the set
vegetables.remove("apple")          #removes apple from the set
#fruits.clear()                     #clears the set {}

if "banana" in vegetables:          #checks if orange is a member.
    print("Orange was found")
else:
    print("Not found")



vegetable = input("Enter a vegetable to search for: ")

if vegetable in vegetables:
    print(f"{vegetables} was found.")
else:
    print("Not found.")              #checks if your input is in the set.



# DICTIONARY {}  

