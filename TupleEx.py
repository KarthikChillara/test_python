"""
Tuple is similar to list except objects in tuple are immutable means we cannot change the elements once assigned
we create Tuple is created using parenthesis syntax
"""
# Various ways of creating tuple
T_Strings = ("Success", "Doesn't", "Have", "Any", "Shade", "Trees")
print(T_Strings)
# T_Strings[0] = 'New String'
"""
TypeError: 'tuple' object does not support item assignment , this error will be thrown if we mention like in line 8
"""
T_Numbers = (10, 20, 30, 50, 60)
print(T_Numbers)
T_Mixed = (10, "Success", 30.9, 30 + 5j, [10, 20, "Karthik", ["Hello", "Hi", [100, 200]]], ['A', 'B'])
"""
List inside tuple can be modified but tuple inside tuple cannot be modified
"""
for val in T_Mixed:
    print(val, "is a", type(val))
T_Mixed[4][1] = 200
print(T_Mixed)
T_Mixed[4][3][1] = "Welcome"
print(T_Mixed)
T_Mixed[4][3][2][1]= 2000
print(T_Mixed)
T_Mixed[5][0]="Apple"
print(T_Mixed)
#Tuple using Constructor
My_Val = tuple(("Chennai","Nellore","Hyderabad"))
print(My_Val)
#Empty tuple
My_Val1 = ()
print(My_Val1)
#Single val tuple
Single_val = (2)#For single element to make python understand its tuple comma should be given else it will treat as respective data type
print(Single_val,type(Single_val))
# del My_Val
# print(My_Val)
print(T_Strings[1:5])
print("Success" in T_Strings)