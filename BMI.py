weight = float(input("enter your weight:"))
height = float(input("enter your height:"))
bmi = weight / (height * height)
if bmi < 18.5:
    print("underwight")
elif bmi >= 18.5 and bmi < 25:
    print("normal")
elif bmi >= 25 and bmi < 30:
    print("overweight")
else:
    print("obesity")