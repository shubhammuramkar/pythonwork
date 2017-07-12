active = True
while active:
	people = input("how many people are in their dinner group :")
	people = int(people)
	if people >8:
		print("You to wait for a table\n")
		QU = input("Enter Quit for exit ")
		if (QU == Quit) or (QU == quit):
			active = False
	else:
		print("Your table is ready.")
		QU = input("Enter Quit for exit ")
		if (QU == "Quit") or (QU == "quit"):
			active = False

