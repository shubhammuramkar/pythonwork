from condition import requested_toppings
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
for item in requested_toppings:
	if item in available_toppings:
		print("Adding " + item)
	else:
		print("Sorry! we don't have " + item )
print("\n Finished")