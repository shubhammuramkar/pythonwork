import json

filename = "usernames.json"
with open(filename) as f:
	username = json.load(f)
	print("Welcome back, " + username + "!")