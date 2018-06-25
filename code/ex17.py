# loading pakages
from sys import argv
from os.path import exists #commend return 'true' if a file exists 'false' otherwise

#ask users to provide script, file names
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do this on one line, how?
# read files use read and open open
in_file = open(from_file)
indata= in_file.read()

# string formating to print out the length of indata file, indata comes from_file
print(f"The input file is {len(indata)} bytes long")

print (f"Does the output file exist? {exists(to_file)}")
print("Ready, hit Return to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()
