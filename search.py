"""
This is a program that generates a list of random numbers, the user can then search whether or not a number appears in the list, and if so how many times and where.
Finally a message is printed letting the user know the result.
"""

from random import seed
from random import randrange

values = []

for i in range(10):
    value = randrange(11)
    values.append(value)

print(values)
number = input("Enter the number you want to search for: ")

number = number.strip()

while not number.isdigit():
    number = input("The value you enter must be a number: ")

number = int(number)

if number in values:
    times = values.count(number)
    print(f"The value {number} appears in the list {times} time/s.")
else:
    print(f"The value {number} is not contained in the list.")

for i in range(len(values)):
    if values[i] == number:
        print(f"The value appears in place {i}")
