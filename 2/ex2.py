import operator

dic = {"A":12,"B":88,"Y":99,"C":10}
print(dic)
print(dic.keys())
print(dic["A"])
li = list(dic.keys())
li.sort()
print(li,type(li))

city = {}
city["A"] = [{"C":80}]
print(city)
city["A"].append({"B":10})
print(city) 
# city["A"].sort() #dict 끼리 <,>가 안되는데 ㅋㅋㅋㅋ
print(city)

city2 = {}
city2["A"] = {"C":100}
print("==========\n",city2)
(city2["A"])["B"]=200
print(city2)
(city2["A"]) = sorted(city2["A"].items(),key=operator.itemgetter(0))
print(city2) # ? list가 되버림..

cc = [{"A":100},{"B":200}]
# cc.index("A")
li = []
li.append(list(cc[1].keys()))
print(li)
print(li.index(['B']))
