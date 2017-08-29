sandwich_orders = ["pastrami","hot","pastrami","tuna","pastrami",]
finished_sandwiches = []
while sandwich_orders:
	sand = sandwich_orders.pop()
	print("I made your " + sand + " sandwitch.")
	finished_sandwiches.append(sand)
for san in finished_sandwiches:
	print("your " + san + " is ready")
print("Thankyou.")

