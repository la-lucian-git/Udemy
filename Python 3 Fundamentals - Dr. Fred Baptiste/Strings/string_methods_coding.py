message = "Just another Python file."

print(message.upper())
print(message.lower())

print('abc' == 'ABC')

print('abc'.lower() == 'ABC'.lower())

print('abc'.casefold() == 'ABC'.casefold())

name = "Peter "
print(name.lstrip())

name = "\t Peter\tJones\t"
print(name)
print(name.strip())


print("Python" + " rocks" + "!")

data = "Jones,Peter"
first_name, last_name = data.split(',')
print(first_name, last_name)

data = ["item 1", "item 2", "item 3"]
print(', '.join(data))

print("rock" in "Python rocks!")
