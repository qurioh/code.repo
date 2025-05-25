def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

print("Welcome to calculator, Select choice (1/2/3/4):"
"1. Add\n"
"2. sub\n"
"3. mul\n"
"4. div\n")

sel = int(input("select operation (1-4). "))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if sel == 1:
    print(n1, "+", n2, "=", add(n1, n2))

elif sel == 2:
    print(n1, "-", n2, "=", sub(n1, n2))

elif sel == 3:
    print(n1, "*", n2, "=", mul(n1, n2))

elif sel == 4:
    print(n1, "/", n2, "=", div(n1, n2))

else:
    print("Invalid Input")




