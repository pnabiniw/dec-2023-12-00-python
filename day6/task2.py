"""
Write a Python function to check whether a number
falls within a given range.
"""


def is_in_range(num, ran):
    return num in ran
    # if num in ran:
    #     return True
    # else:
    #     return False


num = int(input("Enter a number "))
in_range = is_in_range(num, range(10, 25))
print(in_range)
