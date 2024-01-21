print(1 + 0.5)
print(2 * 1.125)
print(18 / 4)
print(2 ** 8)
print(2 ** (-8))
print(4 ** 0.5)
complex_number = (-4) ** 0.5
print(complex_number)
print(complex_number.real)
print(complex_number.imag)

a = 1
print(a.__add__(2))  # Everything is an object


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v_1 = Vector(1, 1)
v_2 = Vector(2, 3)

print(v_1)
print(v_2)
print(v_1 + v_2)







