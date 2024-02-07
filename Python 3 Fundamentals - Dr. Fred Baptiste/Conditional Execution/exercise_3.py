# Given a credit score `score`, assign a string value to another variable `rating` based on the following scale:

# - [0, 580] --> Poor
# - [580, 670] --> Fair
# - [670, 740] --> Good
# - [740, 800] --> Very Good
# - [800, 850] --> Excellent

score = 470

if score < 580:
    rating = 'Poor'
elif score < 670:
    rating = 'Fair'
elif score < 740:
    rating = 'Good'
elif score < 800:
    rating = 'Very Good'
else:
    rating = 'Excellent'

print(rating)

print("\n")
score = 900
rating = 'Poor' if score < 580 else 'Fair' if score < 670 else 'Good' if score < 740 else 'Very Good' if score < 800 \
    else 'Excellent'
print(rating)

