#http://www.pythonforbeginners.com/python-on-the-web/parsingjson/



import json
import pprint
json_data = open("json_file")
 
# the value returned from json.load is a Python dictionary. 
data = json.load(json_data)
 
# use pprint to make the output more readable
pprint.pprint(data)
json_data.close()
 
# Get the data you want, by navigating the structure using standard python.
print data["maps"][0]["id"]
print data["masks"]["id"]
print data["om_points"]
