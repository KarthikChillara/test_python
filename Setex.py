"""
Set is collection which is unordered,unchangeable and unindexed .
Note: Existing value cannot be modified but you can add items and remove items.
Set is created within {}
You cannot have duplicate values
"""
MySet1 = {"SPB", "JANAKI", "Kishore Kumar", "Mohd Rafi", "SPB", "JANAKI"}
print(MySet1, type(MySet1), len(MySet1))
MySet2 = {10, 30, 40, 60, 70, 50, 10, 10}
print(MySet2, type(MySet2), len(MySet2))
MySet3 = {10, 50, 30 + 5j, True, False, "Permit", "Success", "Success", True, 50}
print(len(MySet3))
for value in MySet3:
    print(value, type(value))
# Using Set Constructor
MySet4 = set(("India", "China", "Japan", "Australia"))
print(MySet4)
print("West Indies" in MySet4)
# Adding elements to set
MySet4.add("South Africa")  # Add element to set
print(MySet4)
SomeList = ["Rajiv Gandhi Airport", "Chatrapthi Sivaji Terminal"]
MySet4.update(
    MySet1)  # Add any iterable object (Set,tuple,list,dict) to another set.In this eg My set 1 will be added to MySet4
print(MySet4)
MySet4.update(SomeList)
print(MySet4)
# Removing elements from the set
MySet4.remove("China")  # Remove method will execute if exists, if not exists it will throw error
print(MySet4)
# MySet4.remove("China123")
# print(MySet4)
MySet4.discard("Japan")
print(MySet4)
MySet4.discard("Japan123")  # Discard will not throw error if element not exist. If exist it will remove it
print(MySet4)
# PopValue = MySet4.pop()
# print(PopValue)
# MySet4.clear()
# print(MySet4)
# del MySet4
SetA = {"A", "B", "C",1}
SetB = {1, 2, 3,"A"}
SetC = SetA.union(SetB)
print(SetC)
SetD = SetA.intersection(SetB) # Will give new set
print(SetD)
# SetA.intersection_update(SetB) #Updating existing set
# print(SetA)
SetE = SetA.symmetric_difference(SetB) # Will give new set
print(SetE)
SetA.symmetric_difference_update(SetB) # Updating existing set
print(SetA)
SetF = SetA.copy()
print(SetF)
SetG = {2,3}
print(SetG.issubset(SetF))
print(SetF.issuperset(SetG))
SetH= {5,6}
print(SetH.isdisjoint(SetF)) #If there is no common elements in Disjoint it will return true otherwise it will return false
