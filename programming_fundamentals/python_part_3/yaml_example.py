import yaml
from pprint import pprint

yaml_example = open("yaml_example.yaml").read()
pprint(yaml_example)

yaml_python = yaml.load(yaml_example)
pprint(yaml_python)

int_name = yaml_python["ietf-interfaces:interface"]["name"]
int_desc = yaml_python['ietf-interfaces:interface']['description']
#int_ip = yaml_python['ietf-interfaces:interface']['ietf-ip:ipv4']['address']['ip']
pprint(int_name)
pprint(int_desc)
#pprint(int_ip)
