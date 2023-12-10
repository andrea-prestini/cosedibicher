
try:
    x = int(input("x: "))
    y = int(input("y: "))
    result = x / y
except ZeroDivisionError:
    print("Can't divide by zero")
    exit(1)
except ValueError:
    print("x and y must be numbers")
    exit(1)

print("x / y = ", result)