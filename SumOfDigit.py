str = input("please enter:")
d = 0
a = 0
for i in str:
    if i.isdigit():
        d += 1
    elif i.isalpha():
        a += 1
    else:
        pass
print("letters=", a)
print("digits=", d)
