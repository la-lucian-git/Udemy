for i in range(100):
    print(i)
    if i >= 5:
        print("breaking out of loop.")
        break
print("done")

print("\n")

for i in range(1, 10):
    if i % 2 == 1:
        continue
    print(i)


print("\n")

for i in range(1, 10):
    if i % 2 == 0:
        print(i)


print("\n")

for i in range(1, 5):
    for j in range(1, 5):
        if (i + j) % 2 == 1:
            print(f"{i} + {j} is odd, skip...")
            continue
        print(f"adding numbers: {i} + {j} = {i + j}")
