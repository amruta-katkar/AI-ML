# lecture 6 --> Array operations
from array import *

# 1.reverse order program using for loop

print("Enter size of an array")
n = int(input())
arr = array('i', [0]*n)
for i in range(n):
    print("Enter element", i, ":", end=" ")
    arr[i] = int(input())
print("Original array is: ", end=" ")
for i in range(n):
    print(arr[i], end=" ")


print("\nReverse array is: ", end=" ")
for i in range(n - 1, -1, -1):
    print(arr[i], end=" ")
    
# 2.reverse order program using while loop
print("# 2.reverse order program using while loop")
i=n-1
while i>0:
    print(arr[i], end=" ")
    i-=1


# 2.largest of element using for
max_num = arr[0]
print("\nLargest element is")
for j in range(1,len(arr)):
    if arr[j]>max_num:
        max_num = arr[j]
print(max_num)



# 3. smallest of element

small_num = arr[0]
print("\nSmallest element is")
for j in range(1,len(arr)):
    if small_num>arr[j]:
        small_num = arr[j]
print(small_num)
#  4. print even and odd no using for loop
print("\nEven and odd no in array")

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        print(arr[i], "is even")
    else:
        print(arr[i], "is odd")

