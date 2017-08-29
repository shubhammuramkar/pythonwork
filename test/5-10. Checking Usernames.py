current_user = ["admin","jon","BOSS","cool","hot"]
new_user = ["admin","mac","boss","captain","rock"]
for menber in new_user:
	if (menber.upper() in current_user) or (menber in current_user):
		print("the person will need to enter a new username.".title())
	else:
		print("the username is available.".title())
