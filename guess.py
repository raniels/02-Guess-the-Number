#!/usr/bin/python3

import sys, random

assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

print("Hello and Welcome to Guess That Number! RNG Edition")

u = int(input("Please Select a level: 1, 2, 3, 4, 5")) # asks the users to select a level and converts the string into an integer

if u == 1: z = 10
elif u == 2: z = 20
elif u == 3: z = 30
elif u == 4: z = 40
elif u == 5: z = 50

#variables
n = z
guesses = 0

#generate a random integer between 1 and 20 (inclusive) and store it in the variable [number]
number = random.randint(1,n)

while not guesses >= 10:

		guesses = 1 + guesses

		#ask the user for a response and store it in the variable [guess] and converts it into an integer
		guess = int(input())

		#check if the guess is less than the random number
		if guess < number:

			#gives the user feedback based on their guess
			if guess < (number - 10): hint = ("Try a (much) larger number!")
			if (number - 10) <= guess <= (number - 5): hint = ("Try a (slightly) larger number")
			elif number > guess > (number - 5): hint = ("You're really close though, try guessing a tiny bit higher!")
			print('You guessed wrong! Try again!' + hint)

		elif guess > number:

			# gives the user feedback based on their guess
			if guess > (number + 10): hint = ("Try a (much) smaller number!")
			if (number + 10) >= guess >= (number + 5): hint = ("Try a (slightly) smaller number")
			elif number < guess < (number + 5): hint = ("You're really close though, try guessing a tiny bit lower!")
			print('You guessed wrong! Try again!' + hint)
		elif guess == number:

			print("Gratz! You did it!")
			break

if guesses >= 10:
	print("Mission failed, we'll get em next time")


