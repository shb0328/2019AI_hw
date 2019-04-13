import collections
import pprint

dic = {}

dic["A"] = 8
dic["B"] = 10
dic["Z"] = 9
print(dic)
dic["C"] = 88
print(dic)
pprint.pprint(dic)
print(dic)

od = collections.OrderedDict(sorted(dic.items()))

print(od,od["A"])
for k,v in od.items() : print (k,v)
