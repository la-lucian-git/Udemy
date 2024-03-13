d = {'a': 1, 'b': 2, 'c': 3}

print(d)
print("\n")

person = {
    'first_name': 'Eric',
    'last_name': 'Idle',
    'year_born': 2016
}

print(person)
print(person['year_born'])
person['year_born'] = 1943
print(person)
person['month_born'] = 3
print(person)
print('\n')

d = {3.14: 'pi', 2: 'even', 'prime': 7}
print(d)
print(d[3.14])
print('\n')

# print(hash([])) ---> list are not hashable

t = (1, 2, 3, 4)
print(hash(t))  # tuples are hashable if their elements are hashable

t = ([1, 2], 3, 4)
# print(hash(t))  # tuples are not hashable if the contain un-hashable elements
print('\n')

d = {'a': 1, 'b': 2, 'c': 3}
print(d)
del d['a']
print(d)
print('\n')


print(globals())
print(globals()['person'])

