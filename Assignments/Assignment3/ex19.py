# defined a function named cheese_and_crackers, this function requires two arguments: cheese_count and boxes_of_crackers.
# the cheese_and_crackers function prints 4 lines. The two arguments provided by the user will be assigned to the first and second line.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# print the sentence
print("We can just give the function numbers directly:")
# call function cheese_and_crackers that we defined above. the two arguments are 20 and 30.
cheese_and_crackers(20, 30)


print("OR, we can use varibales from our script:")
# define two variables
amount_of_cheese = 10
amount_of_crackers = 50

# call function cheese_and_crackers, the two arguments are the two variables defined above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# call function cheese_and_crackers, the first argument is the result of 10 + 20 and the second is 5 + 6
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# call function cheese_and_crackers, the first argument is variable amount_of_cheese + 100, the second is varibale amount_of_crackers + 1000
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("Now you give the numbers:")
# call function input and ask user to provide numbers which will be assigned to variables how_many_cheese and how_many_crackers
how_many_cheese = input("cheese number: ")
how_many_crackers = input("cracker number: ")
cheese_and_crackers(how_many_cheese, how_many_crackers)
