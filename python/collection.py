# collection module
# from collections import chainmap
# d1 = {'a': 1, 'b': 2}
# d2 = {'b': 3, 'c': 4}

# ordered dict
from collections import OrderedDict
d1 = OrderedDict([('a', 1), ('b', 2)])
d2 = OrderedDict([('b', 3), ('c', 4)])
print(d1,d2)


import statistics as stats
data = [20,40,38,90,80,90,47,90,28]
print(stats.mean(data))
print(stats.mode(data))
print()

