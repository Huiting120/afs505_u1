# assign numbers to variables.
people = 10
cars = 40
trucks = 15


# if the Boolean expression is true, execute the print function.
if cars > people:
    print("We should take the cars.")
# if the Boolean expression above is False, then move to the elif statement and execute the print function if this Boolean expressions is true.
elif cars < people:
    print("We should not take the cars.")
# if neither of the above Boolean expression us true, execute the following print function.
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
