def world(city,country,population = ''):
	if population:
		full = city + ", " + country + "-" + str(population)
	else:
		full = city + ", " + country
	return full.title()

l = world("Santiago","Chile")
print(l)
q = world("Santiago","Chile",5000000)
print(q)