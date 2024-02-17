from copy import deepcopy

# Shallow copy
l1 = [1, 2, 3]
l2 = l1[:]

print(l1)
print(l2)
print(f"l1 is l2: {l1 is l2}")
l2.append(100)
print(l1)
print(l2)

print("\n")
m1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(f"m1: {m1}")
m2 = m1.copy()
print(f"m2: {m2}")
print(f"m1 is m2: {m1 is m2}")
m2.append([10, 20, 30])
print(f"m1: {m1}")
print(f"m1: {m2}")

print("\n")
print(f"m1[0]: {m1[0]}")
print(f"m2[0]: {m2[0]}")
print(f"m1[0] is m2[0]: {m1[0] is m2[0]}")

print("\n")
m2[0].append(-1)
print(f"m1: {m1}")
print(f"m2: {m2}")

# Deepcopy
print("\n")
m1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(f"m1: {m1}")
m2 = deepcopy(m1)
print(f"m1: {m2}")
print(f"m1[0]: {m1[0]}")
print(f"m2[0]: {m2[0]}")
print(f"m1[0] is m2[0]: {m1[0] is m2[0]}")

print("\n")
m2[0].append(10)
print(f"m1: {m1}")
print(f"m2: {m2}")
