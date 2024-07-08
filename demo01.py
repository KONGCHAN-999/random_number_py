import random

# Generate a list of 10 random integers between 1 and 10000
random_numbers = [random.randint(1, 1000000) for _ in range(1000)]

print("List of 10 random numbers:", random_numbers)
