# Given the following string:
# s = 'FfEeDdCcBbAa'

# Create two new variables that contain just the lower and upper case letters of `s` respectively, in the correct
# alphabetical order, i.e:

# 'ABCDEF'
# 'abcdef'

s = 'FfEeDdCcBbAa'
reversed_s = s[::-1]
print(reversed_s)
lower_letters = reversed_s[::2]
upper_letters = reversed_s[1::2]
print(lower_letters, upper_letters)


