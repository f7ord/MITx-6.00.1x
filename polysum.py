import math

def polysum(n, s):
    """
    n: the number of sides (an integer)
    s: the length of each side (an integer)
    
    returns: the sum of the area and square
    of the perimeter of the regular polygon,
    rounded to 4 decimal places
    """
    area = (0.25*n*s*s) / math.tan(math.pi/n)
    perimeter = n*s
    
    return round(area + (perimter**2), 4)
