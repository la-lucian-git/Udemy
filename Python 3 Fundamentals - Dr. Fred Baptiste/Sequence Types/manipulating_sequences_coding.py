from timeit import timeit

l1 = [10, 20, 3, 40, 50]
print(l1)
l1[2] = 30
print(l1)

print("\n")
l2 = [1, 20, 30, 5, 6]
print(l2)
l2[1:3] = [2, 3, 4]
print(l2)

print("\n")
l3 = [1, 2, 3, 4, 5, 6]
print(l3)
l3[1:3] = 'Python'
print(l3)

print("\n")
l4 = [1, 2, 3, 4, 5, 6, 7, 8]
print(l4)
l4[1::2] = 20, 40, 60, 80
print(l4)

print("\n")
l5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l5)
l5 = l5[:-3:-1]
print(l5)
l5[:-3:-1] = 100, 200
print(l5)

print("\n")
l6 = [1, 2, 3, 4, 5, 6]
print(l6)
del l6[::2]
print(l6)

print("\n")
l7 = [1, 2, 3, 4]
print(l7)
l7.append(5)
print(l7)

print("\n")
l8 = [1, 2, 3, 4]
print(l8)
l8.append([5, 6, 7, 8])
print(l8)


print("\n")
l9 = [1, 2, 3, 4]
print(l9)
l9.extend([5, 6, 7, 8])
print(l9)


print("\n")
l10 = [1, 2, 3, 4]
print(l10)
l10.insert(1, 100)
print(l10)

print("\n")
lst = []
print(timeit('lst.append(1)', globals=globals(), number=100_000))
print(len(lst))

print("\n")
lst = []
print(timeit('lst.insert(0, 1)', globals=globals(), number=100_000))
print(len(lst))
