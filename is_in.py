def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphaetized string (sorted in alphabetical order)

    returns: True if char is in aStr; False otherwise
    """
    if len(aStr) <= 1:
        return char == aStr
    
    mid = len(aStr) // 2
    if aStr[mid] == char:
        return True
    elif aStr[mid] < char:
        return isIn(char, aStr[mid+1:])
    else:
        return isIn(char, aStr[:mid])

print(isIn('a', 'palindrome'))
print(isIn('y', 'palindrome'))
print(isIn('A', 'palindrome'))
print(isIn('f', 'palindrome'))
print(isIn('a', ''))
