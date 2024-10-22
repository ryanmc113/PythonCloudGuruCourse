
num = int(input('Put in a number now!! '))
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fib(n - 2) + fib(n - 1)

finalNum = fib(num)
print(finalNum)