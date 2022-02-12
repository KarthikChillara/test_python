Mixed_List = [10, 50, "abc", 56 + 9j, "tgd", 70]
print(Mixed_List, type(Mixed_List))
Mixed_List[0] = 100
print(Mixed_List)
Mixed_List.insert(5, 80)
print(Mixed_List)
Mixed_List.append(40)
print(Mixed_List)
Mixed_List.reverse()
print(Mixed_List)
NumOfCounts = Mixed_List.count("tgd")
print("The number of counts", NumOfCounts)
