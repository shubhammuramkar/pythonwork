def city_country(city , country):
	detail = city.title() + ", " + country
	return detail
full_detail = city_country("Santiago","Chile")
print('"' +full_detail + '"')
