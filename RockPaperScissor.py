user_answer1 = input("rock,paper,scissor:")
user_answer2 = input("rock,paper,scissor:")


def compare(u1, u2):
    if u1 == u2:
        print("it is tie")
    elif u1 == "rock":
        if u2 == "paper":
            print("paper wins")
        else:
            print("rock wins")
    elif u1 == "paper":
        if u2 == "rock":
            print("paper wins")
        else:
            print("scissor wins")
    elif u1 == "scissor":
        if u2 == "rock":
            print("rock wins")
        else:
            print("scissor wins")
    else:
        print("incorrect input")
        

compare(user_answer1, user_answer2)
