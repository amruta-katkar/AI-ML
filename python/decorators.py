# /lecture 5 --> Decorators

# create decorator
def my_decorator(func):
    def inner():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return inner()
def Ordinaryfunc():
    print("Hello, world!")
dfun = my_decorator(Ordinaryfunc)
dfun()
