def accept_items(*item):
	print("Added Items are ")
	for it in item:
		print("-" + it)

accept_items("pepperoni")
accept_items('mushrooms', 'green peppers', 'extra cheese')
