import json
#with open('APP\Especies copy.JSON') as especies_file:
#  especies = json.load(especies_file)

especies_from_JSON = open('APP\Especies copy.JSON', "r")
especies = especies_from_JSON.read()
especies_list = [json.loads(especies)]
print(especies_list[0]['plantas'][0]['Nombre'])