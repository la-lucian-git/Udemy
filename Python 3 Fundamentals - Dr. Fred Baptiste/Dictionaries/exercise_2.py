# Given the following dictionaries:
#
# d1 = {'a': 10, 'b': 20, 'c': 30}
# d2 = {'d': 100, 'e': 200, 'f': 300}
# d3 = {'f': 30, 'g': 40}

# Construct two lists, one containing all the keys of both dictionaries, and one containing all the values of each
# dictionary. (It is OK for values or keys to be repeated in the lists).

from itertools import chain

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'d': 100, 'e': 200, 'f': 300}
d3 = {'f': 30, 'g': 40}


all_keys = []
all_values = []

for key_, value_ in chain(d1.items(), d2.items(), d3.items()):
    all_keys.append(key_)
    all_values.append(value_)

print(all_keys)
print(all_values)
