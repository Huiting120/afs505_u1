from sys import exit

def rabbit_hole():
	print("""
		You've entered the rabbit hole, what do you want to do next?
		1. kill all the rabbits
		2. look around
		3. exit
		4. I don't know.
		""")

	choice = input("> ")

	if "kill" in choice:
		print("Good job, you found food! Let's go home with the rabbits.")
		exit(0)
	elif "look" in choice:
		dead("The rabbits saw you and killed you.")
	elif "exit" in choice:
		start()
	elif "don't know" in choice:
		dead("Indecisive Homo sapiens die.")
	else:
		dead("Didn't you read my question?")

def pig_house():
	print("""
		You've entered the pig village and see all the pigs are sleeping.
		The pig king is sleeping in front of a door labeled: treasure.
		What do you do?
		1. poke the pig king.
		2. look around.
		3. exit
		""")

	pig_king_moved = False

	while True:
		choice = input("> ")

		if choice == "poke the pig king" and not pig_king_moved:
			print("Do you want to enter the treasure room? y/n")

			desicion = input("> ")
			if desicion == "y":
				dead("It's a lie, there is no treasure, but a monster.")
			elif desicion == "n":
				print("You are a cautious person, good job. what do you do next? choose from the same options like last time.")
				pig_king_moved = True
			else: 
				dead("Didn't you read my question?")

		elif choice == "poke the pig king" and pig_king_moved:
			dead("Why do you keep poking the pig king, now he is annoyed.")
		
		elif choice == "look around" and not pig_king_moved:
			print("You found a secret portal. Enter or not? y/n")

			desicion = input("> ")
			if desicion == "y":
				cat_cafe()
			elif desicion == "n":
				print("Well... OK. What's your next move then?")
				pig_king_moved = True
			else:
				dead("I said! Didn't you read my question?")

		elif choice == "look around" and pig_king_moved:
			dead("You should have ran away since your movement has waken up the pig king and he is annoyed.")

		elif choice == "exit":
			start()
		else:
			dead("I said! Didn't you read my question?")



def cat_cafe():
	print("This is the cat cafe! Best choice of your life! Enjoy!")
	exit(0)


def dead(why):
	print(why, "You suck!")
	exit(0)

def start():
	print("You entered a cave.")
	print("There is a road to your left and your right.")
	print("Which way do you go?")

	choice = input("> ")

	if choice == "left":
		rabbit_hole()
	elif choice == "right":
		pig_house()
	else:
		dead("You stumble around the cave until you starve.")

start()