# lecture 5 -- > inheritance type

# single level inheritance
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Child(Parent):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    def show(self):
        super().show()
        print(f"Grade: {self.grade}")

child = Child("John", 10, 5)
child.show()

# using multilevel inheritance print full name
class Fname:
    def __init__(self, first_name):
        self.first_name = first_name
class Lname(Fname):
    def __init__(self, first_name, last_name):
        Fname.__init__(self,first_name)
        self.last_name = last_name
class Fullname(Lname):
    def __init__(self, first_name, last_name):
        Lname().__init__(first_name, last_name)
    def show(self):
        print(f"Full Name: {self.first_name} {self.last_name}")
obj = Fullname("John", "Doe")



# hierachical
# hybrid
# multiple inheritance