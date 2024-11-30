def isPalindrome(s):
    s = s.lower()
    s = ''.join(x for x in s if x.isalpha())
    
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and isPalindrome(s[1:-1])


print(isPalindrome('Able was I, ere I saw Elba'))
print(isPalindrome('madam'))
print(isPalindrome('palindrome'))
