# Given two floats `a` and `b`, and some tolerance `tol`, write an expression that will test whether `a` and `b` are
# within `tol` of each other.

a = 0.1 + 0.1 + 0.1
b = 0.3
tol = 0.0001

print(f"a = 0.1 + 0.1 + 0.1: {a}")
print(f"b = 0.3: {b}")
print(f"a == b: {a == b}")
# abs(a-b) calculates the distance between a and b
print(abs(a - b) < tol)
