# 18. Find a package in the Python standard library for dealing with JSON.
# Import the library module and inspect the attributes of the module.
# Use the help function to learn more about how to use the module.
# Serialize a dictionary mapping 'name' to your name and 'age' to your
# age, to a JSON string. Deserialize the JSON back into Python.
import json

dict = {
    'name': 'sulochan thapa',
    'age': 22
}

students = json.dumps(dict)
print(type(students))

detail_dict = json.loads(students)
print(type(detail_dict))
