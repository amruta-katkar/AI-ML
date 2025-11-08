# # lecture 4--> exception handelling
# 1.try-except
# 2.else
# 3.finally
# 4.assert
# 5.raise

try:
    print(4/2)
    print(2/0)
except ZeroDivisionError:
    print("you can't divide by zero")
else:
    print("no exception occurred")
finally:
    print("this will always run")

# raise

num = int(input("Enter number : "))
if num >100 :
    raise Exception ("number is greater than 100")
else:
    print("number is less than 100")

# assert
def divide(a,b):
    assert b != 0, "can't divide by zero"
    print(a/b)
divide(10,4)    
divide(10,0)





