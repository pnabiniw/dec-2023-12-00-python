# All those functions which are already defined in python are Python built-in functions

print("Hello World")

len([1, 2, 3, 4])

sum([1, 2, 3, 4])  # 10

max([10, 12, 30, 1, 3, 21])  # 30

min([10, 12, 30, 1, 3, 21])  # 1

data = sorted([10, 12, 30, 1, 3, 21])  # 1, 3, 10, 12, 21, 30
print(list(data))

data = sorted([10, 12, 30, 1, 3, 21], reverse=True)  # 30, 21, 10, 3, 1
print(list(data))

data = reversed([10, 12, 30, 1, 3, 21])
print(data)  # 21, 3, 1, 30, 12, 10


