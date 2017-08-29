def animals(file):

	try:
		with open(file) as f:
			content = f.read()
	except FileNotFoundError:
		print("Sorry! " + file + " is not found. ")
	else:
		print(content)




animals("cats.txt")
animals("dogs.txt")



