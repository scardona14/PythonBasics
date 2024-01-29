import random

# Genarate a random list with randit between 1 and 1000
# Use range to genarate 100 values
randList = list(random.randint(1, 1001) for i in range(100))

# Use modulus to find multiples of 9
print(list(filter((lambda x: x % 9 == 0), randList)))
