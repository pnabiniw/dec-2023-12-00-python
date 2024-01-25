# JSON stands for Javascript Object Notation
# It looks similar to python dictionary.
# It is a data format which can be used fo communication between two or more entities

import json

student = {'name': 'Jon', 'age': 20, 'email': 'j@email.com'}  # dictionary

s = {"name": "Jon", "age": 20, "email": "j@email.com"}  # a valid JSON

filename = "student.json"

with open(filename, "w") as fp:
    data = json.dumps(student)
    fp.write(data)

students = [
    {"name": "Jon", "age": 20, "email": "j@email.com"},
    {"name": "Jane", "age": 22, "email": "jane@email.com"},
    {"name": "Hary", "age": 24, "email": "hary@email.com"}
]

with open("students.json", "w") as fp:
    data = json.dumps(students, indent=2)
    fp.write(data)
