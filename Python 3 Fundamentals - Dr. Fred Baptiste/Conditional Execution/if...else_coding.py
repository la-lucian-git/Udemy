if 1 < 2:
    print("1 is less than 2")

print("\n")

if 1 < 2:
    print("block - line 1")
    print("block - line 2")
    print("block - line 3")
print("next line")

print("\n")

if 1 < 2:
    print('1 is less than 2')
else:
    print('1 is not less than 2')

if 1 > 2:
    print('1 is less than 2')
else:
    print('1 is not less than 2')


account_enabled = True
balance = 1000
withdraw = 100

print("\n")

if account_enabled and withdraw <= balance:
    print("Authorized!")
else:
    print("Not authorized!")


balance = 90

if account_enabled and withdraw <= balance:
    print("Authorized!")
else:
    print("Not authorized!")


if account_enabled and withdraw <= balance:
    print("Authorized!")
else:
    if not account_enabled:
        print("Account disabled")
    else:
        print("Insufficient funds")

print("\n")

grade = 72

if grade >= 90:
    letter_grade = 'A'
else:
    if grade >= 80:
        letter_grade = 'B'
    else:
        if grade >= 70:
            letter_grade = 'C'
        else:
            if grade >= 60:
                letter_grade = 'D'
            else:
                letter_grade = 'F'

print(letter_grade)

grade = 67

if grade >= 90:
    letter_grade = 'A'

if 80 <= grade < 90:
    letter_grade = 'B'

if 70 <= grade < 80:
    letter_grade = 'C'

if 60 <= grade < 70:
    letter_grade = 'D'

if grade < 60:
    letter_grade = 'F'

print(letter_grade)
