def make_album(artist_name,album_title,number = ''):
	movie_Album = {"Artist": artist_name.title(),"Title":album_title.title()}
	if number:
		movie_Album["numbers"] = number
	return movie_Album
# album = make_album("arjit","bass")
# print(album)
# album1 = make_album("sonu","rock",number = 23)
# print(album1)
# album2 = make_album("shubham","cool")
# print(album2)


while True:
	print("Enter an Artist Name , Album Title : ")
	print("(Enter q for exit)")
	ar = input("Artist Name : ")
	if ar == "q":
		break
	al = input("Album Title : ")
	if al == "q":
		break
	detail = make_album(ar,al)
	print(detail)


