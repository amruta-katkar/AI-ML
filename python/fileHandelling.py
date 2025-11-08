# lecture 4 --> file handelling
# write in file
file = open("sample.txt","w")
file.write("Hello, this is a sample file.")
file.close()

# double writing
file = open("sample.txt","w")
file.write("Hello, this is a sample file.")
file.write("next write mode")
file.write("hi")
file.write("hello")
file.close()

# read mode
info = open("sample.txt","r")
print(info.read())
for i in info:
    print(i)

# append mode
info = open("sample.txt","a")
info.write("appended text")
info.close()

info = open("sample.txt","r")

print(info.read())
for i in info:
    print(i)

# with
with open("sample.txt","r") as data:
    i = data.read()
    print(i)

# with split
with open("sample.txt","r") as data:
    i = data.read().split()
    print(i)
