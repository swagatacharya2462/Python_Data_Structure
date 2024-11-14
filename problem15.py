# Implement a code to find and remove duplicates from a list while preserving the original order of elements.

from collections import OrderedDict

list1 = [10, 30, 50, 20, 40, 30, 50]
list1 = list(OrderedDict.fromkeys(list1))
print(list1)
