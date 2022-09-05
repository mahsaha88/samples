def histogram(items):
    for n in items:
        output = ''
        time = n
        while time > 0:
            output += "*"
            time = time - 1
        print(output)


histogram([2, 3, 6, 5])