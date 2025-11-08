# # lecture 4--> types of functions
def show():
    print("Hello, I am a function")

show()

# function with args and return

def square(x):
    return x*x

print(square(5))

# default parameter
def greet(name = "world"):
    print("Hello, " + name)

greet()

# multi return
def greet(name = "world"):
    return "Hello, " + name, "How are you?"
print(greet())

# multiple parameter
def show(*args):
    for arg in args:
        print(arg)

show("hi",1,2,3,4)

# Anonymous function
square = lambda x: x*x 
print("Anonymous function square of 5",square(5))

# filter
seq = [4,6,2,4,2,87,13,5,2,345,4]
even = list(filter(lambda x: x%2==0,seq))
print(even)

# map
def square(n):
    return n*n
num = (2,3,1,4,5,6)
res = map(square,num)
print(list(res))