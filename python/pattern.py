# pattern
n = 4
for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end=" ")
    print()

# half reverse pattern

n = 4
for i in range(n,0,-1):
    for j in range(0,i):
        print("* ",end=" ")
    print()
     

# pattern
# ****
# *  *
# *  *
# ****

n = 4
for i in range(0,n):
    for j in range(0,n):
        if i == 0 or i == n-1:
            print("* ",end=" ")
        elif j == 0 or j == n-1:
            print("* ",end=" ")
        else:
            print(" ",end=" ")
    print()

 

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *