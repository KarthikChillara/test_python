"""
List is collection of items. It is used to store multiple items in single variable.List defined in square braces []
Type - what kind of data types Python interpreter is treating
List items are ordered and changeable.It allows duplicate values and list items are always indexed and index begins with 0
"""
Country_List = ['India', 'USA', 'UAE']
print(Country_List, "is a", type(Country_List))
for country in Country_List:
    print(country, type(country))
Number_List = [10, 20, 30, 40]
print(Number_List, "is a", type(Number_List))
for number in Number_List:
    print(number, type(number))
Mixed_List = [10, 30.50, 'Karthik', 3 + 4j, 30.50, 'Karthik', 10]
print(Mixed_List, "is a", type(Mixed_List))
for Mixed in Mixed_List:
    print(Mixed, type(Mixed))
print(Mixed_List[2])
Mixed_List.append(20)
print(Mixed_List)
Mixed_List.insert(2, 35)  # Insert specify index and then value
print(Mixed_List)
Mixed_List[0] = 100  # update
print(Mixed_List)
# Mixed_List.clear()
# print(Mixed_List)
Mixed_List.reverse()
print(Mixed_List)
NumOfCounts = Mixed_List.count("Karthik")
print("Number of times", NumOfCounts)
print("Length of list :", len(Mixed_List))
pos1, pos2 = 1, 3
Mixed_List[pos1], Mixed_List[pos2] = Mixed_List[pos2], Mixed_List[pos1]
print(Mixed_List)
Empty_List = []
print(Empty_List)
# Using Constructor to create new list
My_List = list((10, 20, 30))
print(My_List)
print(My_List[2])
print(My_List[-2])  # Accessing elements from right hand side
"""
Index as positive begins from 0 and left hand side . For eg in line 38 , 10 is at 0 index, 20 is at 1 index, 30 at index 2
Index as negative begins from -1 and right hand side. For same eg , 30 is at -1 index, 20 is at -2 index, 10 at -3 index
"""
NumList1 = [1, 2, 4, 10, 20, 70, 98, 26, 68]
print(NumList1)
print(NumList1[1:4])  # Slicing Begins list items from 1 to 3. Right hand index value will be excluded
print(NumList1[4:])  # Begins from 4 till end
print(NumList1[:5])  # From beginning till 4th index
NumList1.extend([44, 5, 29])
print(NumList1)
NumList1[0] = 100 #Update only one index value
NumList1[1:3] = [25, 45]  # Updating multiple values at the same time by giving range values
print(NumList1)
del NumList1[4]
print(NumList1)
# del NumList1 #Deleting whole list
# print(NumList1)
NumList1.remove(100)
print(NumList1)
NumList1.pop() #Just pop will remove the last element
print(NumList1)
NumList1.pop(4) #Pop will remove index element
print(NumList1)
NumList1.clear()
print(NumList1)
