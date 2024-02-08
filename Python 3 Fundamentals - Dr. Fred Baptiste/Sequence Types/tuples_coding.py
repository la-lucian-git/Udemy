tuples_1 = 10, 20, [30, 40]

print(tuples_1)
tuples_1[2][1] = 50
print(tuples_1)

print("\n")
tuple_2 = 1, 2, 3
print(tuple_2)
print(type(tuple_2))
print(len(tuple_2))
print(len(tuple_2) - 1)
# tuple_2[0] = 3.14 # immutable; can't change\update

tuple_3 = ([1, 2], [3, 4])
# tuple_3[0] = 100 immutable; can't change\update
tuple_3[0][0] = 100  # tuples as a collection are immutable but if the elements of the tuple are mutabile they can be up
print(tuple_3)

print("\n")
tuple_4 = [1, 2, 3]
print(tuple_4)
list(tuple_4)
tuple_4[-1] = 4
print(tuple_4)
