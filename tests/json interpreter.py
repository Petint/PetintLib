import json
from PetintLib import Table


def main():
    jsonfile = open("427520.json", 'rt')
    jsondata = json.load(jsonfile)
    jsonfile.close()
    print(jsondata)

    json_table = Table(jsondata, align='ec', height=3, width=25)
    print(json_table.make())


if __name__ == '__main__':
    main()
