def avg(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def funct1():
    n1 = 10
    print("n value is", n1)


def funct2():
    n1 = 20
    print("n value is", n1)
    funct1()

funct1()

print("Welcome")
num1 = int(input("Please enter the number :"))
num2 = int(input("Please enter the number :"))
num3 = int(input("Please enter the number :"))

result = avg(num1, num2, num3)
print(result)
