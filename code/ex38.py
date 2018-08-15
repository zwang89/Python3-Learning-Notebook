the_things = "apples oranges crows telphone light sugar"

print("wait there are not 10 things in that list. let's fix that")
stuff = the_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
            "corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding: ", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now")

print("here we go: ", stuff)
print("let's do somthing with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())  # remove the last item from the list and return it
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
print('#'.join(stuff))
