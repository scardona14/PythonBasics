import random

#Create the list
flipList = []

# Populate the list with 100 Hs Ts
for i in range(1, 101):
    flipList += random.choice(['H', 'T'])

# Output the results
print("Heads :", flipList.count('H'))
print("Tails :", flipList.count('T'))
