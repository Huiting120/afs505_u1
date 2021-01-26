# assigned a string to variable formatter. the string needs 4 variables.
formatter = "{} {} {} {}"

# print the string assigned to variable formatter and the string will take 4 arguments to fill the 4 {} required by the string.
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
