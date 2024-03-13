d = {
    'key 1': 1,
    'key_2': 2,
    3.14: 'pi'
}

for k in d:
    print(k)
print('\n')

for k in d:
    print(f"d[{k}] = {d[k]}")
print('\n')

for v in d.values():
    print(v)
print('\n')

for key_, value_ in d.items():
    print(f"d[{key_}] = {value_}")
print('\n')

print(d)
d['x'] = 100
print(d)
