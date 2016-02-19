# Hi Lo Guessing game
print("Choose a number between 1 and 1000")
print("After each guess, enter:")
print("0 if I got it right")
print("1 if I guessed too low")
print("2 if I guessed too high")
high = 1000
low = 0
g = 0

def take_guess(high, low, guesses):
	guess = (high + low) / 2
	print("My guess is: " + str(guess))
	resp = raw_input("Please enter a 0, 1, or a 2: ")
	if int(resp) == 0:
		print("I guessed it right!")
		print  ("It took " + str(guesses) + " guesses!")
	elif int(resp) ==2:
		high = guess
		take_guess(high, low, guesses +1)
	elif int(resp) ==1:
		low = guess
		take_guess(high, low, guesses +1)
	else:
		print("You entered an invalid number")
		high = 1000
		low = 0
		take_guess(high, low)

take_guess(high, low, 0)