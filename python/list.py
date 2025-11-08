# # List operations
# lst = ["mon","tue","wed",2,3,4,5]
# print(lst[0])  # prints: mon
# print(lst[:])
# print(lst[:3])
# print(lst[2:])
# print(lst[2:-4])
# print(lst[::-1])
# print(lst[-3])

# lst[2:4] = ["fri","sat"]
# print(lst)
# del lst[3]
# print(lst)
# del lst[2:4]
# print(lst)

# del lst  # delete whole list
# # print(lst)

# #####list built in functions

sampleList = [1,[2,3,4,5],6,7,8,9]
print(sampleList[1][2])
print(sampleList[1])

lst =[23,67,90,78,34,45,70,90]
lst.append(30)
print(lst)
lst.insert(4,896)
print(lst)

lst.remove(45)
print(lst)
x=lst.pop()
print(x)
print(lst)
print(lst.index(90))
count=lst.count(90)
print(count)

lst.sort()
print(lst)


#  list comprhension
num = [i*2 for i in range(1,11)]
print(num)

num = [i for i in range(1,11) if i%2==0]
print(num)