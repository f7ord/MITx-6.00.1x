def recurPower(base, exp):
    """
    base: int or float
    exp: int >= 0

    returns: int or float, base^exp
    """
    if exp == 0:
        return 1
    return base * recurPower(base, exp-1)

for i in range(11):
    print(i, recurPower(2, i))
