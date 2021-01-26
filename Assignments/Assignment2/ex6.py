# assign the value of 10 to variable types_of_people
types_of_people = 10
# this f-string is assigned to variable x
x = f"There are {types_of_people} types of people."

# assign the strings binary/ don't to variables named binary/ do_not
binary = "binary"
do_not = "don't"
# assign the f-string to variable y. String inside string.
y = f"Those who know {binary} and those who {do_not}."

# print results of strings assigned to variables x and y
print(x)
print(y)

# print f-string with strings assigned to x and y. String inside string.
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Define variable hilarious as False
hilarious = False
# assign string with an undefined variable to variable joke_evaluation
joke_evaluation = "Isn't that joke so funny?! {}"

# print the string assigned to joke_evaluation with a pre-defined variable
print(joke_evaluation.format(hilarious))

# assign strings to variables w and e
w = "This is the left side of ..."
e = "a string with a right side."

# print result of string w followed by e
print(w + e)
