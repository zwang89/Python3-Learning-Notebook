def add(a, b):
    print(f" Adding {a} +{b}")
    return a + b

def substract(a, b):
    print(f"substracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print (" Let's do some math with just functions!")

age = add(30, 6)
height  = substract(78, 4)
weight = multiply(90, 4)
iq = divide(100, 2)

print(f"age: {age}, height: {height}, weight: {weight}, iq: {iq}")

# a puzzle for the extra credit, type it in anyway
print("here is the puzzle")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

(print (f"what is the the number you get?: {what}"))
