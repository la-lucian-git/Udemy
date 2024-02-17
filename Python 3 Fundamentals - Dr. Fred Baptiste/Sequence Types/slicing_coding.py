s = "Python Rocks!"

print(s[5])
print(s[0:5])
print(s[0:6])

print("\n")
t = 1, 2, 3, 4, 5
print(t[1:4])

l1 = [1, 2, 3, 4, 5]
print(l1[1:4])

print("\n")
l2 = [1, 2, 3, 4, 5]
l3 = l1[0:3]
print(l3)
print(l2 is l3)

l2[0] = 100
print(l2)
print(l3)

print("\n")
l4 = [[0, 0, 0], [1, 1, 2], [2, 2, 2]]
print(l4)
l5 = l4[0:2]
print(l5)
l5[1] = "Python"

print("\n")
print(l4)
print(l5)

print("\n")
print(s[7:])
print(s[:6])

print("\n")
l6 = [1, 2, 3, 4, 5]
l7 = l6[:]
print(l6)
print(l7)
print(f"l6 is l7: {l6 is l7}")

print("\n")
l8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l8[1:8:2])

print("\n")
l9 = [1, 2, 3, 4, 5]
l10 = l9[::-1]
print(l9)
print(l10)
