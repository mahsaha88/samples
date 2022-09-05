import random
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?"
passlen = 8
p = "".join(random.sample(s, passlen))
print(p)