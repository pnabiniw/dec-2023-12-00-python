class Circle:
    def __init__(self, radius):
        self.radius = radius

    def add_radius(self, other):  # self => c1
        return self.radius + other.radius

    def __add__(self, other):  # self => c1
        return self.radius + other.radius


c1 = Circle(10)
c2 = Circle(5)
result = c1.add_radius(c2)
print(result)  # 15

result = c1.__add__(c2)
print(result)
result = c1 + c2
print(result)
