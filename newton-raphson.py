"""
g - (p(g) / p1(g))
g^2 - k / 2g

function: f(x) = 0
f(x) is a continuous differentiable function.
Start with an initial guess, the closer to 0, the better. Then approximate the function by its tangent line, and compute the x-intercept of this tangent line. If the tangent to the curve f(x) at x = xn intercepts the x-axis at xn+1, then the slope is f^1(xn) = (f(xn)-0) / (xn - xn+1)
==> xn+1 = xn - (f(xn) / f^1(xn)).
Repeat until a sufficiently precise value is reached.
Geometrically, (xn+1, 0) is the intercept of the tangent of the graph of f at (x0, f(x0))

This method may not work if there are points of inflection, local maxima or minima around x0 or the root
"""
# p(x) = x^2 - y
epsilon = .01
y = 24.0
guess = y/2.0
num_guesses = 0

print('guess =', guess)
while abs(guess*guess - y) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess**2) - y) / (2*guess))
    print('guess =', guess)

print('num_guesses =', num_guesses)
print('square root of', y, 'is about', guess)
