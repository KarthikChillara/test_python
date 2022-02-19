def IPL():
    print("Mumbai Indians")
    print("Chennai Super Kings")
    print("Kolkata Knight Riders")
    print("Royal Challengers Banglore")


def a(text):
    return text.upper()


def b(text):
    return text.lower()


def greet(c):
    greeting = c("Hi, Welcome to Python learning")
    print(greeting)


def add(*num):
    sum1 = 0
    for n in num:
        sum1 = n + sum1
    print("The sum is :", sum1)


def managers(*manager):
    for manager in manager:
        print(manager)


def employees(**employee):
    for d, e in employee.items():
        print(d, e)


IPL()
greet(a)
greet(b)
add(1, 2)
add(100, 200)
add(150, 140, 130)
managers("Kim", "Winslett", "Micheal", "Jordon")
print("Employees List :")
employees(FN="Deborah", LN="Fitsko", Designation="Product Owner")
employees(FN="Santosh", LN="Kumar", Designation="Project Manager")
employees(FN="Ananth", LN="Duvvari", Designation="Software Developer+")
