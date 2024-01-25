import json


with open("students.json", "r") as fp:
    data = json.loads(fp.read())
print(data)  # [{}, {}, {}]
print(type(data))  # list

name = data[2]["name"]
print(name)
