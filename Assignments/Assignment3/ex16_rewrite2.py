from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

# print("Truncating the file. Goodbye!")
# target.truncate()

# print("Now I'm going to ask you for three lines.")

line1 = "I have a little cat."
line2 = "Her name is milk."
line3 = "She is super cute."

# print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
