# lecture 3 --> factorial of number
def fact() :
    num = int(input("Enter a number: "))
    fact = 1
    if num == 1:
        print("Factorial of", num, "is", fact)
    else :
        for i in range(1,num+1):
            fact = fact * i
        print("Factorial of ", num, "is", fact)