#!/usr/bin/python3
"""0.Creating a Simple Templating Program"""
"""template: the template file with placeholder variables"""
"""attendees: details of the attendies for placing into the placeholder variables in the template file"""
"""creating a file output_X.txt with the template filled with attendees details"""

# from task_00_intro import generate_invitations

def generate_invitations(template, attendees):

    count = 0
    for attendee in attendees:
        # print(attendee["name"])
        # print(attendee["event_title"])
        # print(attendee["event_date"])
        # print(attendee["event_location"])
        # print(f"attendee {count}")
        # data_in_template = template
        data_in_template = template.replace("{name}",attendee["name"]).replace("{event_date}",attendee["event_date"]).replace("{event_location}",attendee["event_location"])
        # data_in_template = data_in_template.replace({"{name}":"hello"})

        with open(f"output_{count}.txt", "w") as file:
            file.write(data_in_template)

        count += 1

# Read the template from a file
with open('template.txt', 'r') as file:
    template_content = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Call the function with the template and attendees list
generate_invitations(template_content, attendees)

