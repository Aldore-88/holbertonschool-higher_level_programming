#!/usr/bin/python3
import csv 
import json

def convert_csv_to_json(csv_file):
    try:
        with open("data.csv", mode="r", newline="") as csvfile:
            csv_data = list(csv.DictReader(csvfile))
        
        with open("data.json", "w") as jsonfile:
            json.dump(csv_data, jsonfile, indent=4)

        return True
    except FileExistsError:
        print(f"Error: File {csvfile} not found")

