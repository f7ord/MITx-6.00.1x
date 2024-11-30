# Write a program that prints the longest substring of s in which the letters occr in alphabetical order
# In the case of ties, print the first substring

def longest_substring(s):
    longest = ''
    word = '{'
    for char in s:
        if word[-1] <= char:
            word += char
        else:
            word = char
        if len(word) > len(longest):
            longest = word
    return longest

# s = 'azcbobobegghakl'
# print(longest_substring(s))
# print(longest_substring('abcbcd'))
print(longest_substring('zxvvwzy'))
print(longest_substring(''))
print(longest_substring('lkj'))