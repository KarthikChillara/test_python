"""
Function is block of code which is executed when called. Function returns value
We can pass some data to function which we are known as arguements or parameters
Function Definition - What function is going to do
Function calling  - Using function
using def keyword followed with name of functions
"""


def myaddress():  # Function definition
    print("Karthik")
    print("Street no 5")
    print("Nellore")
    print("AP")
    print(524003)


def greeting(FN):  # passed 1 arguement FN
    print("Good Day", FN)




def add(num1, num2):  # passed two arguements num1 and num2
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


print("Below is my address")
myaddress()  # Function calling
print("There is supermarket near my home")
print("Deliver goods to below address")
myaddress()  # Function calling
greeting("Karthik")
print("Greetings")
greeting("Suman")
num1 = 40
num2 = 20
result = add(num1, num2)  # Function call is add
print("Sum of num1,num2", result)
result = subtract(num1, num2)
print("Difference of num1,num2", result)

"""
If we do not know number of arguements then we put astreik before the parameter name
"""


def myHobbies(*HobbyList):
    for Hobby in HobbyList:
        print(Hobby)


print("My hobbies in jan 2022")
myHobbies("Music", "Painting")
print("My hobbies in feb 2022")
myHobbies("Music", "Painting", "Horse riding", "Swimming")


def myDegrees(Intermediate, Bachelors, Masters):
    print("My Intermediate done in ", Intermediate)
    print("My Bachelors done in ", Bachelors)
    print("My Masters done in ", Masters)


myDegrees("MPC", "BTECH", "MS")
myDegrees(Masters="MCA", Intermediate="BIPC", Bachelors="BCOM")


# When we do not know how many number of keyword arguements we  pass to function then we use double asterix
# before parameter name in function definition
def myFriends(**Friend):
    for a, b in Friend.items():
        print(a, b)


print("Childhood friends")
myFriends(FN="TOM", LN="Harry")
print("Inter Friends")
myFriends(MPC="MARK", BIPC="LEWIS", CEC="Robert")

"""
Function using default parameter value
"""


def myCountry(CountryName="India"):
    print("I am citizen of ", CountryName)


myCountry("USA")

myCountry()
