# lecture 3 --> leap year
year = int(input("Enter year"))
if(year % 4 == 0) or (year% 100 ==0):
    print(year," is leap year")
else:
    print(year," is not leap year")