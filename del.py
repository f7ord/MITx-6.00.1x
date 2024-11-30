x = 23
epsilon = .01
step = .1
guess = 0.0
num_guesses = 0

while guess <= x:
	if abs(guess**2 - x) < epsilon:
		break
	else:
		guess += step
		num_guesses += 1

print('num_guesses:', num_guesses)
if abs(guess**2 - x) >= epsilon:
	print('Failed')
else:
	print('Succeeded:', guess)