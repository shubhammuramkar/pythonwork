name = ["cool","boss","rock"]
def_city = ["bhopal","agra","delhi"]
def_country = ["India","U.S.A","U.K"]
message = """ I am {name} live in {cit} located/place in {pla} """
def describe_city(name,city,country,mess):
	mes = []
	if len(name) == len(def_city):
		i = 0
		for name in name:
			mes = message.format(name = name.title(),cit = def_city[i].title(),
				pla = country[i].title())
			print(mes)
			i += 1

describe_city(name,describe_city,def_country,message)