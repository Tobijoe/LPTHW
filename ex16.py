from sys import argv

script, filename = argv
print(f"We are going to erase{filename}.")
print("If you dont want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input("?")
print("opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now im going to ask you for three lines.")

line1 = input("Line 1:")
line2 = input("Line 2:")
line3 = input("Line 3:")

print("I'm going to write these into the file.")

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print("And finally we close it")
target.close()
