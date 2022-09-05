str = input("please enter your string:")
str = str.casefold()
rev_str = reversed(str)
if list(str) == list(rev_str):
    print("palindrome")
else:
    print("not palindrome")