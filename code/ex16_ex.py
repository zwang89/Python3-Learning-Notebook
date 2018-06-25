from sys import argv

script, filename = argv

txt = open(filename)

print(f"this is what in {filename}:")
print(txt.read())
