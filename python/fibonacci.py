# lecture 3 --> Fibonacci series

terms = int(input("Enter the number of terms: "))
n1,n2 =0,1
count =0
if terms == 0:
    print("No terms")
elif terms ==1:
    print(n1)
else :
    while terms > count:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count +=1
