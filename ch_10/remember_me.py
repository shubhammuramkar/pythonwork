import json

   # Load the username, if it has been stored previously.
   #  Otherwise, prompt for the username and store it.

filename = "usernames.json"
try:
	with open(filename) as f:
		username = json.load(f)

except FileNotFoundError :
	username = input("Enter your name ")
	with open(filename,'w') as f:
		json.dump(usernames,f)
		print("I will remnember you when you will come back " + username  + "!")
else:
	print("Welcome back, " + username + "!")



# username = input("Enter your name ")

# filename = "usernames.json"
# with open(filename,'w') as f:
# 	json.dump(username,f)
	# print("I will remnember you when you will come back " + username  + "!")



