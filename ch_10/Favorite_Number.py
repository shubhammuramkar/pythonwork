import json

def Enter():
	file = "number.json"
	number = input("Enter your favorite number ")
	with open(file,'w') as f:
		json.dump(number,f)
		print("I will remember your facvorite number ")
	return number

def favorite_number():
	l = Enter()
	try:
		file = "number.json"
		with open(file) as f:
			num = json.load(f)
	except FileNotFoundError :
		return None
	else:
		return print( "I know your favorite number! It's " + num)

favorite_number()