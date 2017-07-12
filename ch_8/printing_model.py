unprinted_degisn = ['iphone case', 'robot pendant', 'dodecahedron']
complete_degisn = []
# while unprinted_degisn:
# 	current = unprinted_degisn.pop()
# 	print("Printing model :" + current)
# 	complete_degisn.append(current)
# print("Complete Degins are")
# for item in complete_degisn:
# 	print(item)

def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current = unprinted_designs.pop()
		print("Printing degisn are " + current)
		completed_models.append(current)

def show(completed_models):
	print("Complete models are  ")
	for item in completed_models:
		print(item)

print_models(unprinted_degisn[:],complete_degisn)   # passing copy of unprinted_degisn [:]
show(complete_degisn)
print(unprinted_degisn)