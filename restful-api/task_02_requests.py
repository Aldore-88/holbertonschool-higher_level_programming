#!/usr/bin/python3
"""2.Consuming and processing data from an API usng Python"""
import requests
import csv


def fetch_and_print_posts():
    """
        Fetches all posts from JSONPlaceholder and prints
    """
    input_url = "https://jsonplaceholder.typicode.com/posts"

    data = requests.get(input_url)
    print(f"Status Code: {data.status_code}")
    # print(data.text)
    # print(data.text)
    # print(f"json data {data.json()}") #data inside of json
    # print(data.json) #refers to the json object with the data
    # print()

    if data.status_code == 200:
        data_json = data.json()
        # print("Success")
        """
        if isinstance(data_json, list):
            for post in data_json:
                print(post["title"])
        elif isinstance(data_json, dict):
            print(data_json["title"])
        """
        for post in data_json:
            print(post["title"])

def fetch_and_save_posts():
    """
        Fetches and saves posts from JSONPlaceholder and saves into posts.csv
    """
    input_url = "https://jsonplaceholder.typicode.com/posts"
    
    data = requests.get(input_url)
    if data.status_code == 200:
        print("Request Success")
    
    all_data = []

    for item in data.json():
        print(item)
        # print(item['id'])
        item_list = {
            'id' : item['id'],
            'title' : item['title'],
            'body' : item['body']
        }
        all_data.append(item_list) #everything into one big list
    # print(all_data)
### something is wrong here
    csv_file = "posts.csv"
    with open(csv_file, "w") as csv_file_obj:
        values = ["id", "title", "body"]
        writer = csv.DictWriter(csv_file_obj, fieldnames=values)
        writer.writeheader()
        writer.writerows(all_data)

# fetch_and_print_posts()
# fetch_and_save_posts()