from sys import argv

#ask readers to input filenames
script, filename =  argv

#pirnt the file name that you want to work with
print(f"We are going to erase {filename}.")
print("If you don't wat that, hit CTRL-C(^).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file ...")
# open the file that provided by the readers with 'write mode'
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
#not necessary since open with 'write mode' will overwrite the file
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1 :")
line2 = input("line 2 :")
line3 = input("line 3: ")

print("I am going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
