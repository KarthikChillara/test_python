"""
Built in DataTypes in Python
Text type data - str
Numeric types - numeric data(int,float,complex)
Sequence types - list,tuple,range
Mapping -  Key Value pair (dict)
set types - set, frozenset
Boolean - True/False(bool)
Binary types - bytes,bytearray,memoryview
Should not use keywords as variable
"""
import keyword
print(keyword.kwlist)
MyVar = '5.10'
print(MyVar)
print(type(MyVar))
MyVar1 = str("Python")
print(MyVar1)
print(type(MyVar1))
MyVar2=int(300)
print(MyVar2)
print(type(MyVar2))