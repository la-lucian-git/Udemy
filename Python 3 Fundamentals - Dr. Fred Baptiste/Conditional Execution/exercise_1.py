# Given a variable `a` (containing any value), re-assign the value `"N/A"` if `a` is `None`, and leave `a` unchanged
# otherwise. Use an `if...else...` statement.

a = 100

if a is None:
    a = 'N/A'

print(a)

a = 'Python'

if a is None:
    a = 'N/A'

print(a)

a = None

if a is None:
    a = 'N/A'

print(a)