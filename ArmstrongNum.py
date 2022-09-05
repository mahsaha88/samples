number = int(input("enter your number:"))
sum = 0
temp = number
lenght = len(str(number))
while temp > 0:
    digit = temp % 10
    sum += (digit ** lenght)
    temp = temp // 10
if sum == number:
    print("this number is armstrong")
else:
    print("this number is not armstrong")
