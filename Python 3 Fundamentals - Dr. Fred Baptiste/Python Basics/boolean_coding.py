print(f"not True: {not True}")
print(f"not False: {not False}")
print(f"True and True: {True and True}")
print(f"True and False: {True and False}")
print(f"False and True: {False and True}")
print(f"False and False: {False and False}")

print("\n")
balance = 1000.0
withdraw = 50.0
withdraw_limit = 500.0
print(f"Balance is : {balance}")
print(f"Withdraw is: {withdraw}")
print(f"Withdraw limit is: {withdraw_limit}")

print(f"(withdraw < withdraw_limit) and (withdraw <= balance): {(withdraw < withdraw_limit) and (withdraw <= balance)}")

withdraw = 600.0
print("\n")
print(f"Withdraw is now: {withdraw}")
print(f"(withdraw < withdraw_limit) and (withdraw <= balance): {(withdraw < withdraw_limit) and (withdraw <= balance)}")
