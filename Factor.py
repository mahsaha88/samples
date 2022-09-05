def factor(num):
    list = []
    for i in range(1, num+1):
        if num % i == 0:
            list.append(i)
    return list


num = int(input("enter your number:"))
print(factor(num))
