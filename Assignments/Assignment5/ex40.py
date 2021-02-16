class Song(object):

	def __init__(self, lyrics):
		# self.lyrics can be self.anything... using self.lyrics make things very confuing. 
		#Basically what is means is you pass your input lyrics to the parameter 
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)


song1 = Song("aaaa")


# set happy_bday to an instance of class Song
happy_bday = Song(["Happy birthday to you",
	               "I don't want to be sued",
	               "So I will stop right there"])

bull_on_parade = Song(["They rally around tha family",
                       "With pockets full of shells"])

# from happy_bday, call the sing_me_a_song function.
happy_bday.sing_me_a_song()

bull_on_parade.sing_me_a_song()