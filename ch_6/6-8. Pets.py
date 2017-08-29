pet_1 = {
	"1.":"dog",
	"2.":"cat",
	"3.":"lion"
}
owner = {
	"a.":"rock",
	"b":"boss",
	"c":"cool"
}

pets = [pet_1,owner]
for pet in pet_1.values():
	for own in owner.values():
		print(pet.title() + " belongs to " + "Mrs/Ms." + own.title())

