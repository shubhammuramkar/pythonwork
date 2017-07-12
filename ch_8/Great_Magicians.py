from Magicians import magicians,show_magicians
print(show_magicians)
d = []
c = d[:]
def make_great(person_1,complete):
	while person_1:
		pers = person_1.pop()
		per = " The great " + pers
		complete.append(per)

def show_magicians(complete,magicians=magicians):
	print("Great Deatils are : ")
	for item in complete:
		print(item)
	print("Original names are ")
	for pe in magicians:
		print(pe)

make_great(magicians[:],c)
show_magicians(c)


