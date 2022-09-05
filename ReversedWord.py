def reversed_word(str):
    for i in range(len(str)-1, 0, -1):
        print(str[i], end = "")


str = input("enter your word:")
reversed_word(str)