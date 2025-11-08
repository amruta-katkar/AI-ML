# a=10
# b=20
# print("adition : ",a+b)
print("Hello \n world")
print("Hello \b world")
print("Hello \r world")
print("Hello \\ world")

# printin format
name = "Amruta"
age = 20

print(name,age)
print("My name is ",name,"and age ",age)
print("My name is %s and age %d"%(name,age))
print("My name is {} and age {}".format(name,age))
print("My name is {0} and age {1}".format(name,age))
print("My name is {x} and age {y}".format(x="Amruta",y=20))

# type conversion
num1 = 100
num2 = 101.2099
sum = num1 + int(num2)
print(sum)

# input()
name=input("Enter name")
print(name)
# swapping numbers
a=6
b=4

print(a,b)
a=a+b
b=a-b
a=a-b
print(a,b)
