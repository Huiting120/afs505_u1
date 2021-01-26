# assigned the number 100 to variable cars
cars = 100
# assigned the floating number 4.0 to variable space_in_a_car
space_in_a_car = 4.0
# assigned the number 30 to variable drivers
drivers = 30
# assigned the number 90 to variable passengers
passergers = 90
# assigned the number calculated from cars - drivers to variable cars_not_driven
cars_not_driven = cars - drivers
# assigned the number assigned to variable drivers to variable cars_driven
cars_driven = drivers
# assigned the number calculated from cars_driven * space_in_a_car to variable carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# assigned the number calculated from passengers / cars_driven to variable average_passengers_per_car
average_passengers_per_car = passergers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passergers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
