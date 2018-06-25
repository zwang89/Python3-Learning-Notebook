from sys import argv

script, input_file =  argv

def print_all(f):
    print(f.read())

# file.seek(*th) is to start to read at the *th charasteristics, the defaul is 0
def rewind(f):
    f.seek(0)

# define function to print out line numbers and the content of that line
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("first let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("let's print thre lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1 # current_line = current_line + 1
print_a_line(current_line, current_file)
