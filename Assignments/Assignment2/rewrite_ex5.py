name = 'Zed A. Shaw'
age = 35
height = 74 # inches
height_in_centimeter = height * 2.54
weight = 180 #lbs
weight_in_kilogram = weight * 0.45
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_in_centimeter} cm tall.")
print(f"He's {weight_in_kilogram} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height_in_centimeter + weight_in_kilogram
print(f"If I add {age}, {height_in_centimeter}, and {weight_in_kilogram} I get {total}.")
