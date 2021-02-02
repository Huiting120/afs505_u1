from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

# in the original code, this is written in two lines as follow:
# in_file = open(from_file)
# indata = in_file.read()
# the new code combined these two into one line, which first opened the from_file, then read the contents and assigned the contents to in_file
in_file = open(from_file, 'r')

print(f"The input file is {len(in_file)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(in_file)

print("Alright, all done.")

out_file.close()
in_file.close()
