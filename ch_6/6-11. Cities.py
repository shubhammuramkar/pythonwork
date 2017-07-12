cities = {
	"canada":{
	"country" : "U.S.A",
	"approximate_population":"12330",
	"fact":"it is a lake of heart"
	},
	"london":{
	"country":"U.K",
	"approximate_population" : "45465",
	"fact":"it is a lake of boss"
	},
	"chicago":{
	"country":"U.S.A",
	"approximate_population":"66443",
	"fact":"it is a lake of brokens"
	}
}
for city,info in cities.items():
	print(city.title())
	for key,info_1 in info.items():
		print(key + " " + info_1  )
	print("\n")




