#!/usr/bin/python3
import csv 
import json

def convert_csv_to_json(csv_file):

    with open("data.csv", mode="r", newline="") as csvfile:
        csv_data = list(csv.DictReader(csvfile))
    
    with open("data.json", "w") as jsonfile:
        json.dump(csv_data, jsonfile)
