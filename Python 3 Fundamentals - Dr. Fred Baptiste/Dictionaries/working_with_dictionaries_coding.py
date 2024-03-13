from copy import deepcopy

data = {
    'open': 100,
    'high': 110,
    'low': 95,
    'close': 110
}

print('open' in data)
print('\n')

data.clear()
print(data)
print('\n')

data = {
    'open': 100,
    'high': 110,
    'low': 95,
    'close': 110
}

print(len(data))
print('\n')

# shadow copy - not the same dict
data_copy = data.copy()
print(data)
print(data_copy)
print(data is data_copy)
data_copy['x'] = 33
print('\n')

print(data)
print(data_copy)
print('\n')

# deep copy - not the same dict
data_copy = deepcopy(data)
print(data_copy is data)
print('\n')

d = {
    'a': [1, 2, 3],
    'b': {
        'x': 0,
        'y': 0
    }
}

data_copy = deepcopy(d)

print(d)
print(data_copy)
d['a'].append(4)
print('\n')
print(d)
print(data_copy)
print('\n')

d = dict(a=1, b=2)
print(d)
print('\n')

d = dict.fromkeys(['open', 'high', 'low', 'close'], 0)
print(d)
print('\n')
