x = 54
epsilon = .01
num_guesses = 0
low = 1.0
high = x
ans = (high + low) / 2.0

while abs(ans**2 - x) >= epsilon:
	num_guesses += 1
	if ans**2 < x:
		low = ans
	else:
		high = ans
	ans = (high + low) / 2.0

print('num_guesses:', num_guesses)
print(ans, 'is close to the square root of', x)