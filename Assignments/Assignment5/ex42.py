## Animal is-a object (yes, sort of confusing) look at the extra credit.
class Animal(object):
	pass

## Dog is-a Animal.
class Dog(Animal):
	## class Dog has-a __init__ that takes self and name parameters.
	def __init__(self, name):
		# Dog has-a name called name.
		# now this is setting up how you can retrive this parameter --> name.
		# In this case, it's assigned to a variable name, and it can be called by using the key --> self.name
		# This is confusing, because the author used the same word for the computer stores this value and how to retrive this value.
		# The self.name can be self.anything.
		self.name = name


## cat is-a animal
class Cat(Animal):
	# Cat has a __init__ that takes self and name parameters.
	def __init__(self, name):
		self.name = name


## Person is-a object
class Person(object):

	def __init__(self, name):
		# Person has-a name called name.
		self.name = name
		# Person has-a pet that is set to None (can not be changed).
		self.pet = None

## Employee is-a Person
class Employee(Person):

	# class Employee has-a __init__ that takes self, name, and salary parameters.
	def __init__(self, name, salary)
	## 
	super(Employee, self).__init__(name)
	self.salary = salary

## class Fish is an object.
class Fish(object):
	pass
## Salmon is-a Fish.
class Salmon(Fish):
	pass

## Halibut is-a Fish.
class Halibut(Fish):
	pass


## rover is-a Dog
rover = Dog("rover")

## Satan is-a Cat
satan = Cat("satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet: satan.
mary.pet = satan

## frank is a Employee, has-a name: Frank, has-a salary: 120000
frank = Employee("Frank", 120000)

## flipper is-an instance of Fish???
flipper = Fish()

## crouse is-an instance of Salmon
crouse = Salmon()

## harry is-an instance of Halibut
harry = Halibut()