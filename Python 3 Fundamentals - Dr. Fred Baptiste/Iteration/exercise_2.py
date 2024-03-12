# data = (
#     ['2021-01-01', 10, 20],
#     ['2021-01-02', 20, 18],
#     ['2021-01-03', -10, 10],
#     ['2021-01-04', 100, 102],
#     ['2021-01-05', 20, 45]
# )

# Your program should:
# 1. Mutate the lists in `data` to add one more element indicating the distance between the two integer numbers (i.e.
# the absolute value fo the difference)
# 2. Determine on which date this newly calculate value was the largest.
# 3. Be able to work for a `data` set containing any number of lists.

data = (
    ['2021-01-01', 10, 20],
    ['2021-01-02', 20, 18],
    ['2021-01-03', -10, 10],
    ['2021-01-04', 100, 102],
    ['2021-01-05', 20, 45]
)


max_spread = data[0][-1]
max_date = data[0][0]

for row in data[1:]:
    if row[-1] > max_spread:
        # found a new high
        max_spread = row[-1]
        max_date = row[0]

print(max_date, max_spread)
