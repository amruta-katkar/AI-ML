# datatypes

# numeric
# boolean
# string
# character
# none

# membership operator

# in -->used to check number is present sequence
# not in used to check value is not present in sequence


# identity operator

# is , is not 
print('2' is not 2)
print (2 is '2')

# conditional statments

# if
num = int(input("Enter number:"))
if num<20:
    print("number is greater than 20")


#  if else
num1 = int(input("Enter number1:"))
num2 = int(input("Enter number2:"))
num3 = int(input("Enter number3:"))

if num1>num2:
    if num1>num3:
        print("number1 is greater")
    else:
        print("number 3 is greater")
elif num2>num3:
    print("number 2 is greater")
else:
    print("num3 is graeter")

# even odd
num = int(input("enter number:"))
if num%2==0:
    print("number is even")
else :
    print("number is odd")

# valid age for work
age = int(input("Enter age"))
if age>20:
    print("you can work with us")
else :
    print("you can not work with us")

# largest number
# sum