# ----------------------------------------
# RANDOM MODULE IN PYTHON
# ----------------------------------------

# THEORY:
# 1. The 'random' module is used to generate random numbers.
# 2. Common functions in random module:
#    - random()        -> returns a random float number between 0.0 and 1.0
#    - randint(a, b)   -> returns a random integer between a and b (inclusive)
#    - randrange(a, b) -> returns a random number from range(a, b)
#    - uniform(a, b)   -> returns a random float between a and b
#    - choice(seq)     -> returns a random element from a sequence (list, tuple, string)
#    - shuffle(seq)    -> shuffles elements of a list in place
#    - sample(seq, k)  -> returns k unique random elements from a sequence

import random

print("RANDOM MODULE EXAMPLES")

# random()
print("Random float (0 to 1):", random.random())

# randint()
print("Random integer (1 to 10):", random.randint(1, 10))

# randrange()
print("Random number from range 0-50 step 5:", random.randrange(0, 50, 5))

# uniform()
print("Random float between 5 and 10:", random.uniform(5, 10))

# choice()
fruits = ["apple", "banana", "cherry", "orange"]
print("Random choice from list:", random.choice(fruits))

# shuffle()
random.shuffle(fruits)
print("After shuffle:", fruits)

# sample()
print("Random sample of 2 fruits:", random.sample(fruits, 2))
