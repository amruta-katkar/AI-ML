# find the n natural numbers
n = int(input("Enter n th natural number to sum: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("Sum of first", n, "natural numbers is:", sum)