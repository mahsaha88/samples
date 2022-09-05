def fibonacci(x):
    m = 0
    n = 1
    if x < 0:
        print("wrong number")
    elif x == 0:
        return m
    elif x == 1:
        return n
    else:
        for i in range(2, x+1):
            o = m + n
            m = n
            n = o
        return n


print(fibonacci(12))
