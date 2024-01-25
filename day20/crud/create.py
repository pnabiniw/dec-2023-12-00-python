import json
import os
filename = "students.json"


def create_student():
    name = input("Enter the name ")
    age = input("Enter the age ")
    address = input("Enter the address ")
    student = {"name": name, "age": age, "address": address}

    if not os.path.exists(filename):
        with open(filename, "w") as fp:
            data = json.dumps([student], indent=2)
            fp.write(data)
    else:
        with open(filename, "r+") as fp:
            data = json.loads(fp.read())
            data.append(student)
            fp.seek(0)
            fp.write(json.dumps(data, indent=2))
