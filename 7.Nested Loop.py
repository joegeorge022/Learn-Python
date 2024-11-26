# 14.NESTED LOOPS

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol: ")


# RECTANGLE
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
print()



#TRIANGLES
print("Pattern-1")
print("---------")
for i in range(1, rows + 1):
        for j in range(i):
            print(symbol, end="")
        print()

print()
print("Pattern-2")
print("---------")
for i in range(rows, 0, -1):
        for j in range(i):
            print(symbol, end="")
        print()

print()
print("Pattern-3")
print("---------")
for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print(symbol, end="")
        print()

print()
print("Pattern-4")
print("---------")
for i in range(rows, 0, -1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print(symbol, end="")
        print()