from random import randint
x = randint(1, 10)


class Die():
	def __init__(self,sides = 0):
		self.sides = sides

	def roll_die(self,times):
		i=1
		i = int(i)
		for i in range(i,self.sides):
			print(i)
			i += 1

d = Die(x)           # run this program atleast 2 times to see the changes
d.roll_die(10)