import json

file  = "number.json"

try:
	with open(file) as f:
		num = json.load(f)
except FileNotFoundError :
	number = input("Enter your favorite number ")
	file = "number.json"
	with open(file,'w') as f:
		json.dump(number,f)
	print("I will remember your favorite number " + str(number))
else:
	print("Your favorite number is " + str(num))