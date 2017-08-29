def count_words(file):
	"""Count the approximate number of words in a file."""
	try:
		with open(file) as f:
			word = f.read()
	except FileNotFoundError:
		# print("Sorry! " + file + " is not exit")
		pass
	else:
		l = word.split()
		q = len(l)
		print("Total word in " + file + " is : " + str(q) )

file = "ch_10/text_file/alice.txt"
count_words(file)


file = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in file:
	count_words(filename)