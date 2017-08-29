responses = {}
# name3 = input("What is your name :")
# location = input("If you could visit one place in the world, where would you go? :")
active = True
while active:
	# name = name3         we will not do like this we have to write input in while block
	# place = location
	name = input("What is your name :")
	place = input("If you could visit one place in the world, where would you go? ")
	responses[name] = place
	repeat = input("Would you like to continue (yes/no)")
	if repeat == "no":
		active = False

print("-----Dream vacation are------")
for name_1,place_1 in responses.items():
	print(name_1 + " want to travel " + place_1)
print("Thankyou")