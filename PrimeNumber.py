num1 = int(input("Please enter the number:"))
flag = False
if num1 > 1:
    i = 2
    while i <= num1 / 2 + 1:
        if num1 == 2:
            flag = True
        elif num1 % i == 0:
            flag = False
            break
        else:
            flag = True
        i += 1
elif num1 == 1:
    print("1 is neither prime nor composite")

else:
    print("num1 is not prime number")
if not flag:
    print("num1 is not prime number")
else:
    print("num1 is prime number")
