# define function to print out functions
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# give values direct to function
print("We can just give functin numbers directly:")
cheese_and_crackers(20, 30)

# define function by using variables and call the values based on number you give
# to the variables
print("We can just use varaibles from our script:")
amount_of_cheese = 10
amount_of_crackers = 150

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
