"""
Availability of variable from inside of region
"""
num1 = 500 #Global variable and scope is within whole program
def funct1():
    num2 = 100 #Local variable to function 1 and scope is also within funct1
    print(num2)
    global num1 #Access variable defined in line 3 global scope
    print(num1)
    num1 = 1000
    print(num1)



funct1()
print(num1)