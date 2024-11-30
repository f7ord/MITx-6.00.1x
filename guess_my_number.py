# The user thinks of an integer between 0 (inclusive) and 100 (inclusive).
# The computer then guesses the number

secret_num = print('Please think of a number between 0 and 100!')
print("Enter 'h' to indicate the guess is too high.\n\
Enter 'l' to indicate the guess is too low.\n\
Enter 'c' to indicate I guess correctly.")
low, high = 0, 101

while True:
	guess = (low + high) // 2
	response = input(f'Is your number {guess}? ')
	if response == 'c':
		print('Game over. Your secret number was', guess)
		break
	elif response == 'h':
		high = guess
	elif response == 'l':
		low = guess
	else:
		print('Sorry, I did not understand your input')
	
	if (low == high) and response != 'c':
		print('There is no number left to guess')
		break
	print('low:', low, 'high:', high)
