import json
from PetintLib.autotable import Table

jsonfile = open("427520.json", 'rt')
jsondata = json.load(jsonfile)
jsonfile.close()
print(jsondata)

json_table = Table(jsondata, width=20)
print(json_table.make())
