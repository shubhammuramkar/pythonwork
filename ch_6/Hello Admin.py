message = "Hello {name}, thank you for log- ging in again."

menber = ["admin","jon","boss","cool","hot"]
for people in menber:
	if people == "admin":
		print("Hello "+ people + " would you like to see a status report?")
	else:
		new = message.format(name = people.title())
		print(new)
print("Thank you.Have a nice ")
