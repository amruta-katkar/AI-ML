# lecture 5 -->class, oops concepts
class Demo:
    def __init__(self):
        print("This is Demo class")

d = Demo()

class Sample:
    company = "Google"
    def __init__(self,name):
        self.name = name
        print("My name is {}".format(self.name))

obj = Sample("Rahul")

class Add:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print( self.a + self.b)

a= Add(10,20)
print("object a=of add class",a)

