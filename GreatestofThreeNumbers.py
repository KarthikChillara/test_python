num1 = input("Please enter the number n1 :")
num2 = input("Please enter the number n2 :")
num3 = input("Please enter the number n3 :")

if num1 > num2:
    if num1 > num3:
        print("Num1 is greatest")
    else:
        print("Num3 is greatest")
elif num2 > num1:
    if num2 > num3:
        print("Num2 is greatest")
    else:
        print("Num3 is greatest")
elif num1 == num2:
    if num1 == num3:
        print("All numbers are equal")

