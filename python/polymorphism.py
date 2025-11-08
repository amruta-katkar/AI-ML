# lecture 5 --> polymorphism
class Birds:
    def fly(self):
        print("Birds can fly")
class Sparrow(Birds):
    def fly(self):
        print("Sparrow can fly")
class Eagle(Birds):
    def fly(self):
        print("Eagle can fly")

obj = Birds()
obj.fly()  
obj = Sparrow()
obj.fly()  
obj = Eagle()
obj.fly()  