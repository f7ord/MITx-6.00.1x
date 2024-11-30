def bin_whole_num(num):
    """Convert a whole number (decimal) into binary"""
    if num < 0:
        is_neg = True
        num = abs(num)
    else:
        is_neg = False

    result = ''
    if num == 0:
        result = '0'
    while num > 0:
        result = str(num%2) + result
        num = num // 2

    if is_neg:
        result = '-' + result
    return result


def bin_float(num):
    """Compute the binary representation of a floating-point number"""
    # Find an integer p such that (2**p)*x is a whole number
    p = 0
    while ((2**p)*num) % 1:
        p += 1
    x = int(num*(2**p))

    # calculate the binary representation of (2**p)*x
    result = bin_whole_num(x)

    # to make p == len(result)
    for i in range(p - len(result)):
        result = '0' + result
    
    result = '.' + result
    # result = float(result) / (10**p)

    return result


# num = -45
# print(bin_whole_num(num))
print(bin_float(.375))
print(bin_float(.333))
print(bin_float(.39767))
