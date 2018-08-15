the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a flat_list
for number in the_count:
    print(f"this is count {number}")

# same above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go rhought mixed lists too
# notice we have to use { since we do not do what's in it
for i in change:
    print(f"i got{i}")

# we can also build lists, first start we do not kow with an empty One
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 5):
    print(f"adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"elements was: {i}")

n = 3
m = 2
a = [[0] * 3] * m
b = [i for sublist in range(0, len(a)) for i in range(0, len(a[sublist]))]
print(b)
print(a)
print(len(a))
