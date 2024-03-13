# Use a dictionary to count the frequency of the characters `a-z A-Z` in a given string.
#
# You should write your code to be as general as possible, so that it will work with any string of any given length.
#
# Your resulting dictionary should only contain keys for characters that occurred at least once (i.e. no zero count
# characters should be present.)
#
# Hint: you will probably want to use the `ord()` function that we studied earlier along with the unicode character
# codes for `a`, `z`, `A` and `Z`.

# For example, if the given string is:
#
# ```
# s = 'Aa, Bb - A a B C'
# ```
#
# then your resulting dictionary should be:
#
# ```
# {
#     'A': 2,
#     'a': 2,
#     'B': 2,
#     'b': 1,
#     'C': 1
# }
# ```


s1 = """
“'And' and 'or' are the basic operations of logic. Together with 'no' (the logical operation 
of negation) they are a complete set of basic logical operations — all other logical 
operations, no matter how complex, can be obtained by suitable combinations of these.” 
― John von Neumann, The Computer and the Brain
"""

d = {}

for string in s1:
    if string not in d.keys():
        d[string] = 1
    else:
        d[string] += 1

print(d)
