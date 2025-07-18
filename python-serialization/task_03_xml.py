#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    tree = ET.parse(dictionary)
    root = tree.getroot()
    print(tree)
    print(root)
    print(filename)

sample_dict = {
    'name': 'John',
    'age': '28',
    'city': 'New York'
}

xml_file = "data.xml"
serialize_to_xml(sample_dict, xml_file)