
favorite_languages = {
   'jen': 'python',
   'sarah': 'c',
   'edward': 'ruby',
   'phil': 'python',
   }
# for name, lan in favorite_languages.items():
# 	print("Name : " + name.title())
# 	print("Language : " + lan.title() + "\n")

# for name, language in favorite_languages.items():
# 	print(name.title() + "'s favorite language is " +
#         language.title() + ".")



# ## for printing key value only
# for name in favorite_languages.keys():
# 	print(name.title())



# message = """      Hello, {name} your favorite language is  """
# friend = ['phil','sarah']
# for name in favorite_languages.keys():
# 	print(name.title())
# 	if name in friend:
# 		l = len(name)
# 		new = message.format(
# 			name = name.title()
# 			)
# 		print(new + favorite_languages[name].title())



## it will give the result in sorted manner
# for name in sorted(favorite_languages.keys()):
#    print(name.title() + ", thank you for taking the poll.")

 ## it will print only value!!!!
print("The following languages have been mentioned:")
i = 1
for language in favorite_languages.values():
	print(str(i) + "." +language.title())
	i += 1



## use of non repeated value
print("The following languages have been mentioned:")
i = 1
for language in set(favorite_languages.values()):
	print(str(i) + "." +language.title())
	i += 1
