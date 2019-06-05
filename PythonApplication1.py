
import json

with open("airports.json", "r") as f:
    data = json.load(f)

with open("newdoc.json","w+") as outfile:
	for i in data:
		if i['type'] == "airport" and i['size'] == "large" and i['name'] != None:
			json.dump(i, outfile)
			outfile.write("\n")