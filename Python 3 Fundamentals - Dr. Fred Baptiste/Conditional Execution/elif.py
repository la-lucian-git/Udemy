grade = 87

if grade >= 90:
    print(f"Passed with {grade}, distinction!")
elif grade >= 70:
    print(f"Passed with {grade}, above average!")
elif grade >= 60:
    print(f"Passed with {grade}, average!")
elif grade >= 50:
    print(f"Passed with {grade}, you got lucky!")
else:
    print(f"Failed with {grade}, try again!")

print("\n")

account_enabled = True
balance = 1000
withdraw = 100

if not account_enabled:
    print("Authorized!")
elif withdraw > balance:
    print("Insufficient funds!")
else:
    print("Withdrawal authorized")
