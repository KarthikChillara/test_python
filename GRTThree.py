num1 = input("Please enter the number n1 :")
num2 = input("Please enter the number n2 :")
num3 = input("Please enter the number n3 :")

if num1 > num2 and num1 > num3:
    print("num1 is greatest")
elif num2 > num1 and num2 > num3:
    print("num2 is greatest")
elif num1 == num2 and num1 == num3:
    print("All three are equal")
else:
    print("Num3 is greatest")