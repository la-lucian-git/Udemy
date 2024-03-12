suites = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

for suite in suites:
    print(f"{suite[0].upper()} : {suite}")

print('\n')

for c in 'Python':
    print(c)

print('\n')

for i in range(2, 11, 2):
    print(i)


print('\n')


for i in range(3):
    for j in range(3):
        print(f"i : {i}; j: {j}")
    print('-' * 15)


m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


for row_index in range(3):
    for column_index in range(3):
        print(f"[{row_index}, {column_index}] = {m[row_index][column_index]}")

print('\n')

m = [
    [0, 1],
    [2, 3, 4, 5, 6],
    [7, 8, 9],
    [10]
]


for row_index in range(len(m)):
    for column_index in range(len(m[row_index])):
        print(f"[{row_index}, {column_index}] = {m[row_index][column_index]}")
