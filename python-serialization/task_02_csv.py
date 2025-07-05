#!/usr/bin/python3
"""2. Converting CSV Datat to JSON Format"""
import csv 
import json

def convert_csv_to_json(csv_file):
    """
        Converting csv data to json
        
        Returns:
            Boolean
    """
    try:
        with open("data.csv", mode="r", newline="") as csvfile:
            csv_data = list(csv.DictReader(csvfile))
            print(csv_data)

        with open("data.json", "w") as jsonfile:
            json.dump(csv_data, jsonfile)

        return True

    except FileExistsError:
        print(f"Error: File {csvfile} was not found")
        return False
    except Exception as e:
        print(f"Error {e}")
        return False