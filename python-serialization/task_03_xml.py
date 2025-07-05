#!/usr/bin/python3
import xml.etree.ElementTree as ET
import json

def serialize_to_xml(dictionary, filename):
    tree = ET.parse('movies.xml')
    root = tree.getroot()
    