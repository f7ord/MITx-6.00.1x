# Write a program that prints the number of times a string occurs in s.

def count(ss, s):
    """
    ss is the substring to count
    s is the string
    """
    ss_len = len(ss)
    count = 0

    for i in range(len(s)):
        if s[i: i+ss_len] == ss:
            count += 1
    return count


s = 'azcbobobegghakl'
print(count('bob', s))

print(count('bob', ''))
print(count('d', s))
print(count('',s))