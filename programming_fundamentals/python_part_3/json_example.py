import json
from pprint import pprint

json_example = open("json_example.json").read()
pprint(json_example)

json_dict = json.loads(json_example)
pprint(json_dict)

int_name = json_dict["ietf-interfaces:interface"]["name"]
pprint(int_name)

pprint(json.dumps(json_dict))