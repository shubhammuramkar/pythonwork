import json

def greet_user():
	name = input("Enter your useranme ")
	if name == get_stored_username():
		print("Welcome back, " + name + "!")
	else:
		print("This username is not present in file ")
		username = get_new_username()
		print("We'll remember you when you come back, " + username + "!")


def get_stored_username():
	file = "usernames.json"
	try:
		with open(file) as f:
			name = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return name

def get_new_username():
	file = "usernames.json"
	username = input("Enter your username ")
	with open(file,'w') as f:
		json.dump(username,f)
	return username

greet_user()

