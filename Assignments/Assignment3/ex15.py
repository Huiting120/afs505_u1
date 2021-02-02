# import feature argv from package called system
from sys import argv

# assign 2 variables to argv, the first one is the default one, script, and the second one is the name of a file.
script, filename = argv

# use function open, and create a file handle named txt.
txt = open(filename)

# print the sentence below with the filename provided above.
# print the contents in txt by using the read function.
print(f"Here's your file {filename}:")
print(txt.read())

# print the sentence below:
print("Type the filename again:")
# print > on the screen, and assign a file of your choice to variable: file_again
file_again = input("> ")

# use function open and create a file handle called txt_again.
txt_again = open(file_again)

# print the contents from txt_again, which is the contents of the file of your choice.
print(txt_again.read())
