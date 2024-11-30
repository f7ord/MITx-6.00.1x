def gcdIter(a, b):
    """
    a, b: positive integers
    returns: a positive integer, the greatest common divisor
    """
    d = min(a, b) if ((a != 0) and (b != 0)) else max(a,b)
    while a%d or b%d:
        d -= 1    
    return d


print(gcdIter(2, 12))
print(gcdIter(6, 12))
print(gcdIter(9, 12))
print(gcdIter(17, 12))
print(gcdIter(0, 13))
