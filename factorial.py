def facrorial(n):
    sum = 1
    while n > 0:
        sum *= n
        n -= 1
    return sum


print(facrorial(4))