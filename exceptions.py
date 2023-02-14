import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Invalid value")
    sys.exit(1)

try:
    print(x/y)
except ZeroDivisionError:
    print("Error can not divide by zero")
    sys.exit(1)