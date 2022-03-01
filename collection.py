# from collections import Counter
# a="aabbbccc"
# var=Counter(a)
# print(var.items())
# print(var.keys())
# print(var.values())
# print(var.most_common(1))
from collections import namedtuple
point=namedtuple("point","x,y")
pt=point(2,-4)
print(pt)
from collections import OrderedDict
OrderedDict={}
OrderedDict ["a"] ="gideon "
OrderedDict["b"]=2
OrderedDict["c"]=3
OrderedDict["d"]=4
print(OrderedDict)