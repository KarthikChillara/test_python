"""
Iterator is object that contains countable number of values
Iterator is object that can be iterated upon.You can travese through all values
Iterator is object which implements iterator protocol which consists of method __iter()__ and __next()__
"""
tuple1 = ("Chennai","Hyderabad","Kolkata","New Delhi","Mumbai")
tuple1iter = iter(tuple1)  #Traverse through values
print(next(tuple1iter))
print(next(tuple1iter))
print(next(tuple1iter))
print(next(tuple1iter))
print(next(tuple1iter))

#creates iter object and execute next method for each loop
for somecityname in tuple1:
    print(somecityname)
        