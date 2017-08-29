info = {
	"first_name":"ram",
	"last_name" :"boss",
	"age": str(12),
	"city":"chicago"
        }
people = {
         "name":"ram",
         "surname":"cool"
 }


# print(info)


user_0 = {
'username': 'efermi',
 'first': 'enrico',
              'last': 'fermi',
              }
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

list_1 = [info,people,user_0]

for item in list_1:
	for key,data in item.items():
		print("1." + key.title())
		print("2." + data.title())

