def fibonacci(x):
    fib_array = [0, 1]
    for n in range(2, x+1):
        fib_array.append(fib_array[n-1]+fib_array[n-2])
    return fib_array[x]

    print(fibonacci(13))
