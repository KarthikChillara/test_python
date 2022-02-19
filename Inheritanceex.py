"""
Reusablity and extensibility
"""


class Person:
    def __init__(self, FirstName, LastName, Age):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Age = Age

    def print_person_details(self):
        print("FirstName :", self.FirstName, "LastName :", self.LastName, "Age :", self.Age)


class Student(Person):
    pass


# This init function in line 21 will be called whenever we create object of child class
class Employee(Person):
    def __init__(self, FirstName, LastName, Age, Salary, Designation):
        Person.__init__(self, FirstName, LastName, Age)
        self.Salary = Salary
        self.Designation = Designation

    def print_salary_details(self):
        super().print_person_details()  # Refer to parent class (Super function),make child class inherit all the methods and properties from its parents
        print(self.Salary, self.Designation)

    def print_person_details(self):
        print(self.Salary, self.Designation)


E1 = Employee("SSWQ", "EREE", 45, 25000, "Project Manager")
E1.print_salary_details()
E1.print_person_details()

P1 = Person("Micheal", "Jordon", 40)
P1.print_person_details()
S1 = Student("ABC", "DEF", 25)
S1.print_person_details()
