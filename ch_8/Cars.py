def car_detail(manufacturer_name,model_name,**other):
	detail = {}
	detail["manufacturer_name"] = manufacturer_name
	detail["model_name"] = model_name
	for key, value in other.items():
		detail[key] = value
	return detail
car = car_detail('subaru', 'outback', color='blue', tow_package=True)
print(car)

