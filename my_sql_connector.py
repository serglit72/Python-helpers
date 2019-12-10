import mysql.connector
import json

fh = open("my_json.json", "w+")
mydb = mysql.connector.connect(user='root',password = 'root', database='anchorfree')
cursor = mydb.cursor()

query = ("SELECT id,identity,traffic_limit_type FROM carrier WHERE identity LIKE '%test%'")

mydict = {}
json_key = ()
json_value = ()

cursor.execute(query)

for (row) in cursor:
	json_key = row[0]
	json_value = row[1]
	# print("{}:{}".format(json_key,json_value))
	mydict[json_key] = json_value
fh.write(json.dumps(mydict)) # converts dictionary into JSON object and
							# write into file .json 

print(mydict)

fh.close()
cursor.close()
mydb.close()
