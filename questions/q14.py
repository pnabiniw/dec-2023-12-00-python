"""
What are magic methods? Explain with examples.
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __gt__(self, other):
        return self.radius > other.radius

c1 = Circle(10)
c2 = Circle(20)
print(c1 > c2)


a = 1
b = 2
c = a + b
c = a.__add__(b)
