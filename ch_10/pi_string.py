# filename = 'ch_10/text_file/pi_digits.txt'
# with open(filename) as file_object:
# 	lines = file_object.readlines()
# pi_string = ''
# for line in lines:
# 	pi_string += line.rstrip()     ## "\n" is removed i.e just run above code to see the difference
# print(pi_string)
# print(len(pi_string))


filename = 'ch_10/text_file/pi_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.strip()     ## we replace rstrip() to strip()
print(pi_string[:4] + "...")
print(len(pi_string))














