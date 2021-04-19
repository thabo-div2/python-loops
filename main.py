# Exercise 1
# Loop for 100 times i.e. range
for x in range(101):

    # Number divisible by 15,(divisible
    # by both 3 & 5), print 'FizzBuzz'
    # in place of the number
    if x % 15 == 0:
        print("FizzBuzz")
        continue

    # Number divisible by 3, print 'Fizz'
    # in place of the number
    elif x % 3 == 0:
        print("Fizz")
        continue

    # Number divisible by 5, print 'Buzz'
    # in place of the number
    elif x % 5 == 0:
        print("Buzz")
        continue

    # Print numbers
    print(x)

# Task 1
# Write a program that generates a random number (0-10) and ask you to guess it. You have three asserts.
# Define a random number between 0 - 10.
from random import randint

r = randint(0, 10)
guesses_left = 3 # Initialize guesses_left to 3.

# Use a while loop to let the user keep guessing so long as guesses_left is greater than zero
while guesses_left >= 0:
    guess = int(input("Enter your guess:"))
    if guess == r:
        print("Yay!")
        break
    guesses_left = guesses_left - 1
else:
    print("Loser!")

# Task 2
# Write a Python program to construct the following pattern, using a nested for loop.

n = 5
for x in range(n):
    for y in range(x):
        print ('* ', end="")
    print('')

for x in range(n,0,-1):
    for y in range(x):
        print('* ', end="")
    print('')
