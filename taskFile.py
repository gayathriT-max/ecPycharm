def factorial(n):
    if n < 0:
        return 0
    elif n == 1 or n == 0:
        return 1
    else:
        to_return = 1
        while (n > 1):
            to_return *= n
            n -= 1
        return to_return


print(factorial(5))
