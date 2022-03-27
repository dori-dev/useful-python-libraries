"""json library
"""
# JSON: JavaScript Object Notation
import json

with open("assets/data.json", "r") as school_json:
    school_data = json.load(school_json)

print(type(school_data))
# list
print(school_data[0])
# {'name': 'ali', 'age': 18, 'grades': [20, 19, 20, 15.75], 'address': None}
