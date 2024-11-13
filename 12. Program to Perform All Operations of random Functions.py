import random

# Random integer in range
rand_int = random.randint(1, 100)

# Random float in range
rand_float = random.uniform(1.0, 10.0)

# Random choice from a list
choices = ["apple", "banana", "cherry"]
rand_choice = random.choice(choices)

# Shuffle a list
random.shuffle(choices)

# Generate random sample
rand_sample = random.sample(range(1, 100), 5)

print("Random Integer:", rand_int)
print("Random Float:", rand_float)
print("Random Choice:", rand_choice)
print("Shuffled List:", choices)
print("Random Sample:", rand_sample)
