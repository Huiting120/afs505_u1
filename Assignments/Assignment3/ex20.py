from sys import argv

script, input_file = argv

# define function called print_all. This function read the given file.
def print_all(f):
    print(f.read())

# define function called rewind. This function redirects the file handle to the first byte.
def rewind(f):
    f.seek(0)

# define function called print_a_line. This function prints a variable named line_count, the line that read from a given file.
def print_a_line(line_count, f):
    print(line_count, f.readline())

# define a file handle, current_file, to input_file.
current_file = open(input_file)

print("First let's print the whole file:\n")

# call the print_all function and print the given file.
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# call rewind function so that the file handle goes back to the first byte of the file.
rewind(current_file)

print("Let's print three lines:")

# provide a number, 1, to variable current_line.
current_line = 1
# call function print_a_line, the two arguments provided are: variable -> current_line; and file handle current_file.
print_a_line(current_line, current_file)

# now the value assigned to current_line changed from 1 to 1 + 1.
current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
