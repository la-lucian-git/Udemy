# Do the same problem as Exercise 3, but do **not** mutate `m`.
from copy import deepcopy

m = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

copy_m = deepcopy(m)

copy_m[0][0] = 1
copy_m[1][1] = 1
copy_m[2][2] = 1
print(copy_m)