from sys import argv
# use argv to get the filename
script, filename = argv

# use open function to open the file
txt = open(filename)

# print out the the name of the file and read
print (f"here's your file {filename}: ", end = " ")
print (txt.read())

print ("Typle the file name again:")
# prompt to ask user what is the file name
file_again = input ("> ")

txt_again = open(file_again)
print(txt_again.read())

txt_again.close()
