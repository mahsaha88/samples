def reversed_sentence(str):
    word = str.split(" ")
    word = word[-1::-1]
    return word


str = input("enter our word:")
print(reversed_sentence(str))
