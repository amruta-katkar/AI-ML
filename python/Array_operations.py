# lecture 6 --> Array operations
from array import *
a = array("i",[101,102,103,4,5,6,7])
print(a)

# print using for in loop
for i in a:
    print(i,end = " ")


# using while loop
i = 0
size = len(a)
print("Array using while loop")
while i< size:
    print(a[i],end = " ")
    i += 1

# Array operations
print("Array after Appending")
a.append(10)
a.append(20)
print(a)

print("poped element",a.pop())
a.remove(10)
print("after removing elment",a)
print("Index of 103",a.index(103))
a.insert(3,45)
print("array after inserting",a)
a.reverse()
print(a)


# extending array
a.extend([1,2,3,4,5,6,7,8,9])
print(a)

# user input
size = int(input("enter size of array"))
b = array("i",[])
for i in range(size):
    num = int(input("enter number"))
    b.append(num)
print(b)


a1 = array("i",[1,2,3,4,5,6,7])
b1 = array("i",[10,20,30,40])

print("array before extend")
for i in a1:
    print(i,end = " ")
a1.extend(b1)
print("\narray after extend")
for i in a1:
    print(i,end = " ")


# matrix addition
a = [[1,2,3],[1,2,3],[1,2,3]]
b = [[1,2,3],[1,2,3],[1,2,3]]

c = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        c[i][j] = a[i][j] + b[i][j]

for i in range(len(c)):
    print(c[i])

# Perform matrix multiplication
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j] += a[i][k] * b[k][j]

for i in range(len(c)):
    print(c[i])


# duplicate array elements
arr = [1,2,3,4,5,6,1,2,3]
for i in range (len(arr)):
    print(i,end = " ")
    print()
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] == arr[j]:
            print("duplicate element:",arr[j])

# copy element in another array
arr = [1,2,3,4,5,6,7,8,9]
arr1 = [None]*len(arr)
for i in range(len(arr)):
    arr1[i] = arr[i]
print(arr1)

# transpose matrix
a = [[1,2,3],[4,5,6]]
b = [[0,0],[0,0],[0,0]]
for i in range(len(a[0])):
    for j in range(len(a)):
        b[i][j] = a[j][i]
print(b)




