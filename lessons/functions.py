"""Practice with functions."""

# from random import randint, random, choice

"""
for i in range(10):
    print(randint(3, 17))

for x in range(10):
    print(random())

for q in range(10):
    print(choice("hello"))
"""


# Function Definition
def sum(num1: int, num2: int) -> int:  # <- signature
    """Return the sum of num1 and num2."""
    return num1 + num2


# Function call
print(sum(num1=2, num2=13))  # <- arguments
print(sum(1, 2))  # <- positional arguments
