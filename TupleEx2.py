T_Val2 = ('p', 'e', 'r', 'm', 'i', 't', 23.4, 10)
print(T_Val2)
print(T_Val2[2])
T_Mixed = ("Permit", 23.4, 30 + 5j, [10, 20, "Karthik", ["Hello", "Hi", [100, 200]]], ['Orange', 'Apple'],
           ['Chennai', 'Hyderabad'])
T_Mixed[5][1]='New York'
print(T_Mixed)
T_Mixed[3][3][0] ="Welcome"
T_Mixed[3][3][1]= "to Python training"
print(T_Mixed)
print(T_Val2[1:5])
T_Mixed[4].append("Mango")
print(T_Mixed)