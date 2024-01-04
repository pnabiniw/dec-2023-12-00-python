"""
WAP to delete all the occurrences of a specified character in a given string
S = “All the occurrences of a specified character in a given string”
Input = “a”
Output = “ll occurrences of  specified chrcter in  given string”

"""

s = "All the occurrences of a specified character in a given string"
result = ""
for each in s:
    if each.lower() == "a":
        continue
    result += each

print(result)
