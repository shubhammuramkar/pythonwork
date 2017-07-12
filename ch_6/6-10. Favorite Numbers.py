favorite_number = {
	"Ram":[1,2],
	"boss":[34,56,33],
	"shubham":[18032015]
	}
for name ,number in favorite_number.items():
	print(name.title() + "'s favorite number is/are " )

	for num in number:
		print("\t" + str(num))
