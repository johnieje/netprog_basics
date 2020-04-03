import xmltodict
from pprint import pprint

xml_example = open("xml_example.xml").read()

pprint(xml_example)

xml_dict = xmltodict.parse(xml_example)
int_name = xml_dict["interface"]["name"]
int_description = xml_dict["interface"]["description"]
int_ip = xml_dict["interface"]["ipv4"]["address"]["ip"]

pprint(int_name)
pprint(int_description)
pprint(int_ip)

xmlunparsed = xmltodict.unparse(xml_dict)
pprint(xmlunparsed)
