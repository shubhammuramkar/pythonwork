def animals(file):

	try:
		with open(file) as f:
			content = f.read()
	except FileNotFoundError:
		pass
	else:
		print(content)




animals("cats.txt")
animals("dogs.txt")



