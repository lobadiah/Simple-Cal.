import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

def sin(x):
    # x is in degrees
    return math.sin(math.radians(x))

def cos(x):
    # x is in degrees
    return math.cos(math.radians(x))

def tan(x):
    # x is in degrees
    if x % 180 == 90:
        return "Error: Undefined"
    return math.tan(math.radians(x))

def log(x):
    if x <= 0:
        return "Error: Invalid input"
    return math.log10(x)

def ln(x):
    if x <= 0:
        return "Error: Invalid input"
    return math.log(x)

def sqrt(x):
    if x < 0:
        return "Error: Invalid input"
    return math.sqrt(x)

def factorial(x):
    if x < 0 or not float(x).is_integer():
        return "Error: Invalid input"
    return math.factorial(int(x))

def exp(x):
    return math.exp(x)
