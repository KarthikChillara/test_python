from multipledispatch import dispatch
@dispatch(int,int)
def addition(num1,num2):
    result = num1+num2
    print(result)

@dispatch(int,float,int)
def addition(num1,num2,num3):
    result = num1+num2+num3
    print(result)

addition(10,20)
addition(10,20.5,30)
