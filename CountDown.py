import time
def countdown(t):
    while(t):
        mins, secs = divmod(t, 60)
        timer = '{}:{}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("blast off!!!")


t = input("enter the time in seconds:")
countdown(int(t))