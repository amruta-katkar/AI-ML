# lecture 5 -->Encapsulation
class Base:
    def __init__(self):
        self.a = "Welcome"
        self.b = "to data science"
        self.__c = "this is private variable"
        self._d = "this is protected variable"
        print(self.__c)
        print(self._d)
        
class Subclass(Base):
    def __init__(self):
        Base.__init__(self)
        print("This is subclass")
        print(self.a)
        print(self.b)
        print(self._d)
        try:
            print(self.__c)
        except Exception as e:
            print(e)

obj = Subclass()