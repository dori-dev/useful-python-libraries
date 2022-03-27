"""json library
"""
# JSON: JavaScript Object Notation
import json
from unicodedata import name


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


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class PersonEncoder(json.JSONEncoder):
    def default(self, obj: object) -> dict:
        if isinstance(obj, Person):
            return {
                "__person__": True,
                "name": obj.name,
                "age": obj.age
            }
        return super().default(obj)


def person_decoder(obj: dict) -> object:
    if '__person__' in obj:
        return Person(obj['name'], obj['age'])
    return obj


p1 = Person('zahra', 19)
with open('person_data.json', 'w') as json_file:
    json.dump(p1, json_file, indent=4, cls=PersonEncoder)
with open('person_data.json', 'r') as json_file:
    data = json.load(json_file, object_hook=person_decoder)
print(data)
print(data.name)
