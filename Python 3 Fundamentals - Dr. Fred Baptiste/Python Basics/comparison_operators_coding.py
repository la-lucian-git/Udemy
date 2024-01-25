a = 10
b = 10
c = 10.0

print(f"a is: {a}")
print(f"b is: {b}")
print(f"c is: {c}")
print("\n")
print(f"a == b: {a == b}.")
print(f"a == c: {a == c}.")
print(f"a is c: {a is c}.")
print(f"a is b: {a is b}.")

# Memory address
print("\n")
print(f"ID of a: {id(a)}")
print(f"ID of c: {id(c)}")


# Python is not silly ???
a = 1000000
b = 1000000

print("\n")
print(f"a is: {a}")
print(f"b is: {b}")
print(f"a == b: {a == b}.")
print(f"a is b: {a is b}.")
print(f"ID of a: {id(a)}")
print(f"ID of c: {id(b)}")

print("\n")
print(f"10 != 12: {10 != 12}")
print(f"10.5 != 10.5: {10.5 != 10.5}")
print(f"10 >= 5: {10 >= 5}")
print(f"10 <= 5: {10 <= 5}")
