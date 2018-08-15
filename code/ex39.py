# this chapter is about dictionary
# what does mappning means? associates in python

# create a mapping of state to abbreviation
states = {
         'Oregon': 'OR',
         'Florida': 'FL',
         'California':'CA',
         'New York': 'NY',
         'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
}

# add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print('NY states has:', cities['NY'])
print('OR state has:', cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abb as {abbrev}")

# print cities in states
print('_' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)

state = states.get("Texas")

if not state:
    print("no Texas")

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
