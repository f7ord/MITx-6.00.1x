def fib(x):
    if x == 0 or x == 1:
        return 1
    return fib(x-1) + fib(x-2)

for i in range(11):
    print(i, fib(i))
