file = "alice.txt"

try:
	with open(file) as f:
		data = f.read()
except FileNotFoundError:
	msg = "Sorry, the file " + file + " does not exist."
	print(msg)
else:
	data.split()
	l = len(data)
	print(file + " file have " + str(l) + " words ")