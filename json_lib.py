"""json library
"""
# JSON: JavaScript Object Notation
import json


with open("assets/school_info.json", "r") as json_file:
    school_data = json.load(json_file)
print(type(school_data))
# list
print(school_data[0])
# {'name': 'ali', 'age': 18, 'grades': [20, 19, 20, 15.75], 'address': None}


list_data = [
    1, 2, 3.5,
    'hello', 'wow',
    True, None, False,
    [10, 20, 30],
    {
        "name": "mohammad",
        "age": 21,
    },
    (1, 2, 3, 4)
]
with open('data.json', 'w') as json_file:
    json.dump(list_data, json_file, indent=4)


info_dict = {
    'name': 'salar',
    'age': 16,
    'address': 'Isfahan',
    'grades': (10, 15, 20, 18),
}
with open('info.json', 'w') as json_file:
    json.dump(info_dict, json_file, indent=4)


with open('info.json', 'r') as json_file:
    info = json.load(json_file)
print(info)
