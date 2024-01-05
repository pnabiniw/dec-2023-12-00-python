# Arbitrary Arguments
def addition(*args):
    print(args)
    return sum(args)


s1 = addition(1, 2)
print(s1)  # 3
s2 = addition(1, 2, 3)
print(s2)  # 6
s3 = addition(1, 2, 3, 4)
print(s3)


def addition(**kwargs):
    print(kwargs)
    values = kwargs.values()
    return sum(values)


r1 = addition(a=1, b=2)
print(r1)  # 3
r2 = addition(a=1, b=2, c=3)
print(r2)  # 6
r3 = addition(a=1, b=2, c=3, d=4)
print(r3)  # 10

