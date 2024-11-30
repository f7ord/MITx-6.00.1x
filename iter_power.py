def iterPower(base, exp):
    """
    base: int or float
    exp: int >= 0

    returns: int or float, base^exp
    """
    ans = 1
    while exp > 0:
        ans *= base
        exp -= 1
    return ans


for i in range(11):
    print(i, iterPower(2, i))
