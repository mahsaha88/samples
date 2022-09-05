def hcf(num1, num2):
    if num1 < num2:
        smaler = num1
    else:
        smaler = num2
    for i in range(1, smaler+1):
        if num1 % i == 0 and num2 % i == 0:
            h = i
    return h


def lcm(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    while(True):
        if(greater % num1 == 0 and greater % num2 == 0):
            return greater
        greater += 1
    return greater


num1 = 54
num2 = 24
print(hcf(num1, num2))
print(lcm(num1, num2))