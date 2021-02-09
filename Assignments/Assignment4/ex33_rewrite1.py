def add_number(max_number):
	i = 0
	numbers = []

	while i < max_number:
		numbers.append(i)

		i +=  1

	for num in numbers:
		print(num)


print("Please define your maximum number:")
my_number = int(input())

add_number(my_number)