print("""You enter a dark room with two doors.
Do you go through door #1 or #2?""")

door = input (">")

if door == "1":
    print("There is a gain bear here eating a cheese cake")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear")

    bear = input(">")

    if bear =="1":
        print("The bear eats your face off. Good Job!")
    elif bear =="2":
        print("The bear eats your legs off. Good Job!")
    else:
        print(f"well, doing {bear} is probabaly better.")
        print("Bear runs away.")

elif door =="2":
    print("You state into the endless abyss at retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input(">")

    if insanity == "1" or insanity =="2":
        print("Your body survives powered by a mind of jello")
        print("Goood Job")
    else:
        print("The insanity rots your eyes into a pool of much.")
        print("Good Job")
else:
    print("You stumble around and fall on knife and die")        
