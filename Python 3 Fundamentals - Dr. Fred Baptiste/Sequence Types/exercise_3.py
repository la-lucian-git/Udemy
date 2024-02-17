# Given the following matrix:

# m = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 0, 0]
# ]

# Make this matrix into an identity matrix (setting the diagonal elements to `1`).
# Your code should *mutate* `m`.

m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


m[0][0] = 1
m[1][1] = 1
m[2][2] = 1
print(m)

# for index, a in enumerate(m):
#     print(index, a)
#     a[index] = 1
print(m)
