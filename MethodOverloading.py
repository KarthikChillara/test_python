# def multiplication(num1,num2):
#     result = num1*num2
#     print("Multiplication with 2 arguements",result)

# def multiplication(num1,num2,num3):
#     result = num1*num2*num3
#     print("Multiplication with 3 arguements",result)

#multiplication(3,4) - This is problem with method overloading where it allows same method and pass multiple arguements but it will only take last defined method(latest)

from multipledispatch import dispatch
@dispatch(int,int)
def multiplication(num1,num2):
    result = num1*num2
    print("Multiplication with 2 arguements of type int and int",result)

@dispatch(int,int,int)
def multiplication(num1,num2,num3):
    result = num1*num2*num3
    print("Multiplication with 3 arguements",result)

@dispatch(float,float)
def multiplication(num1,num2):
    result = num1*num2
    print("Multiplication with 2 arguements of type float and float",result)

multiplication(10,20)
multiplication(2.5,3.5)
multiplication(2,3,5)
