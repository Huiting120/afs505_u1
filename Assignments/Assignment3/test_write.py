line1 = "I have a little cat."
line2 = "Her name is Milk."
line3 = "She is super cute."

f = open("test_write_function.txt", "w")
f.write(f"{line1}\n{line2}\n{line3}")

f.close()
