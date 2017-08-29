import csv,shutil
from tempfile import NamedTemporaryFile

def get_length(file_path):
	with open(file_path) as csvfile:
		reader = csv.reader(csvfile)
		reader_list = list(reader)
		return len(reader_list)




def append_data(file_path, name, email):
	fieldname = ["id","name","email"]
	next_id = get_length(file_path)
	with open(file_path,"a") as csvfile:
		writer = csv.DictWriter(csvfile,fieldnames = fieldname)
		#writer.writeheader()
		writer.writerow({
			"id":next_id,
			"name":name,
			"email":email
			})

#append_data("data.csv","shubham","abcdef18032015@gmail.com")

temp_file = NamedTemporaryFile(delete = False)
file_name = "data.csv"
with open(file_name,"rb") as csvfile,temp_file:
	reader = csv.DictReader(csvfile)
	fieldname = ["id","name","email","amount","sent"]
	writer = csv.DictWriter(temp_file,fieldnames = fieldname)
	#writer.writeheader()
	for row in reader:
		writer.writerow({
			"id" : row["id"],
			"name" : row["name"],
			"email" : row["email"],
			"amount" : "12.32",
			"sent" : ""
			})

shutil.move(temp_file.name, file_name)




