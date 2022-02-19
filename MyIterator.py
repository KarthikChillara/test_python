class MyIterator:
    def __iter__(self):
        self.somenum = 1  # Initializing with 1 and returning value 1
        return self

    def __next__(self):
        if self.somenum <=50:
            somenum = self.somenum
            self.somenum += 5
            return somenum
        else:
            raise StopIteration


it1 = MyIterator()
it2 = iter(it1)
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))