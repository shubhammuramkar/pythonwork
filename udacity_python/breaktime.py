import webbrowser , time

total_break = 3
count_break = 0
print("This program start" + time.ctime())

# for t in range(0,3):
# 	new = 2
# 	time.sleep(3)
# 	url = "https://www.youtube.com/"
# 	webbrowser.open(url,new=new)

   #========OR Using WHILE loop======="""


while count_break < total_break:
		new = 2
		time.sleep(3)
		url = "https://www.youtube.com/"
		webbrowser.open(url,new=new)
		count_break += 1