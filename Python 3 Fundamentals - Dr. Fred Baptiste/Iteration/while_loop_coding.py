price = 100

while price > 90:
    print(f"price : {price} ---> wait")
    price -= 1
print(f"buying at {price}")

print('\n')

price = 100
while price < 50:
    print(f"price : {price}")
print("Done!")

data = [100, 200, 300, 400, 500]

print('\n')
print(data)
while len(data) > 0:
    last_element = data.pop()
    print(f"processing element: {last_element}")
    