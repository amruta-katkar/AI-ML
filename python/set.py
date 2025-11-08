# set
s={1,2,3,4,5,6,7,8,9}
print(type(s))


sampleSet = set()
print(type(sampleSet))

# insert value in set
sampleSet.add(10)
sampleSet.add(20)
sampleSet.add(30)
print(sampleSet)

# update set
sampleSet.update([40,50,60])
print(sampleSet)
sampleSet.update(["ABC"])
print(sampleSet)

# list = ["amar","akbar"]
# sampleSet.upadate([list])
# print(sampleSet)