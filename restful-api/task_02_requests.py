#!/usr/bin/python3

import requests

def fetch_and_print_posts(input_url):
    data = requests.get(input_url)
    print(data.text)
    # print(data.text)
    # print(data.json()) #data inside of json
    # print(data.json) #refers to the json object with the data
    # print()

    if data.status_code == 200:
        data_json = data.json()
        # print("Success")
        if isinstance(data_json, list):
            for post in data_json:
                print(post["title"])
        elif isinstance(data_json, dict):
            print(data_json["title"])

def fetch_and_save_posts(input_url):
    data = requests.get(input_url)
        

fetch_and_print_posts("https://jsonplaceholder.typicode.com/todos/1")
