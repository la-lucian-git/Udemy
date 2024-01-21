a = 100  # "=" is an assignment operator not evaluation
print(a)

b = a + 11
print(b)

a = 3.14
print(a)  # variables are variable :)

# Naming conventions
test = 1
_test = 10
test1 = 100
test_1 = 101

# Reserved
# if; float; int; str; etc

a = float(10)
print(a)

# Even tho it's revered you can overwrite float
float = 100.55
print(float)
# however something like: a = float(10) won't work.
del float  # Deleting the label will revert to default behavior.
float = 100.66
print(float)
