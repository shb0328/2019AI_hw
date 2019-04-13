import openpyxl
from pprint import pprint

# 엑셀파일 열기
filename1 = "Assignment 19-2 (straight-line).xlsx"
filename2 = "Assignment 19-2 (distance).xlsx"

straightline_book = openpyxl.load_workbook(filename1)
distance_book = openpyxl.load_workbook(filename2)

# 활성화된 sheet 추출하기
s_sheet = straightline_book.active
d_sheet = distance_book.active

# ================================================ #

"""

decimal 48 = char '0' ~ decinal 57 = char '9'
i = 48~50, j = 48~57, except '00'

"""

# ================================================ #

"""

s_sheet

"""

# 도시 이름 list로 추출
cityNames = []

for i in range(48, 51):
	for j in range(48, 58):
		if (i != 48 or j != 48):
			city = s_sheet["A"+chr(i)+chr(j)].value
			if(city is not None):
				cityNames.append((str(city))[0])

print(cityNames)

# 도시부터 B까지 직선거리 list로 추출
straights = []

for i in range(48, 51):
	for j in range(48, 58):
		if (i != 48 or j != 48):
			straight = s_sheet["B"+chr(i)+chr(j)].value
			if(straight is not None):
				straights.append(straight)

print(straights)

# {도시 : 직선거리, ... ,{}} dict로 만들기
citys = {}

for i in range(0, len(cityNames)):
	citys[cityNames[i]] = int(straights[i])

print("\n************************\ncitys = ")
pprint(citys)

# ================================================#

"""

d_sheet

"""

# A 열의 도시를 출발 key로.
# 도시 이름 list 뽑기.
cityNames.clear()
for i in range(48, 51):
	for j in range(48, 58):
		if (i != 48 or j != 48):
			city = d_sheet["A"+chr(i)+chr(j)].value
			if(city is not None):
				cityNames.append((str(city))[0])
print(cityNames)

# {key(출발 도시) : value{'도착도시':거리,...},...,{} } A->B
nodes1 = {}
for name in cityNames:
	nodes1[name] = {}
print(nodes1)

for i in range(48, 51):
 for j in range(48, 58):
  if (i != 48 or j != 48):
   A = d_sheet["A"+chr(i)+chr(j)].value
   B = d_sheet["B"+chr(i)+chr(j)].value
   Akey = (str(A))[0]
   Bkey = (str(B))[0]
   distance = d_sheet["C"+chr(i)+chr(j)].value
   # print(Akey)
   # print(Bkey)
   # print(distance)
   if(A is not None):
    nodes1[Akey][Bkey] = distance # A->B

print(nodes1)


# B 열의 도시를 출발 key로.
# 도시 이름 list 뽑기.
cityNames.clear()
for i in range(48, 51):
	for j in range(48, 58):
		if (i != 48 or j != 48):
			city = d_sheet["B"+chr(i)+chr(j)].value
			if(city is not None):
				cityNames.append((str(city))[0])
print(cityNames)

# {key(출발 도시) : value{'도착도시':거리,...},...,{} } B->A
nodes2 = {}
for name in cityNames:
	nodes2[name] = {}
print(nodes2)

for i in range(48, 51):
 for j in range(48, 58):
  if (i != 48 or j != 48):
   A = d_sheet["A"+chr(i)+chr(j)].value
   B = d_sheet["B"+chr(i)+chr(j)].value
   Akey = (str(A))[0]
   Bkey = (str(B))[0]
   distance = d_sheet["C"+chr(i)+chr(j)].value
   # print(Akey)
   # print(Bkey)
   # print(distance)
   if(Akey is not None):
    nodes2[Bkey][Akey] = distance # B->A

print(nodes2)

# d_sheet A->B 랑 B->A 합치기(최종)
nodes = {}
for name1 in nodes1.keys():
    print(nodes1[name1])
    for name2 in nodes2.keys():
        if name1 == name2:
            nodes1[name1].update(nodes2[name2])
        else:
            nodes[name2] = nodes2[name2]

nodes.update(nodes1)
print("\n************************\nnodes = ")
pprint(nodes)

"""
알파벳 순서로 정렬된 자식 list를
{key(출발 도시) : value{'도착도시':거리,...,'child':[]},...,{} }
<- 'child':[]로 추가
"""

for name in nodes.keys():
    child = sorted(nodes[name].keys())
    nodes[name]['child'] = child

print("\n************************\nnodes + sorted child list = ")
pprint(nodes)

# ================================================#

"""

BFS

"""
print("\n\n BFS \n\n")

class Queue:

    def __init__(self):
        self.myList = list()

    def enqueue(self, node):
        self.myList.append(node)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.myList.pop(0)
   
    def isEmpty(self):
        if not self.myList:
            return True
        return False

    def size(self):
        return len(self.myList)

    def clear(self):
        self.myList.clear()

    def show(self):
        for i in range(0,len(self.myList)):
            print("[",i,"]",self.myList[i])

    
class Node:

    def __init__(self, data, path=[], cost=0):
        self.data = data
        self.path = path.copy()
        print("node init ... path:",path)
        print("node init ... self.path:",self.path)
        self.path.append(data)
        print("node init ... after append, path:",path)
        print("node init ... after append, self.path:",self.path)
        self.cost = cost

    def showPath(self):
        print(self.path)

    def equal(self, data):
        return self.data == data

    def __str__(self):
        # return "data : "+self.data+", path : "+self.path.__str__()
        return self.data





# right most
start = 'T'
end = 'B'

startNode = Node(start)

open = Queue()
close = Queue()

open.enqueue(startNode)
open.show()

print("\n\nWhile start\n\n")
while open.isEmpty() == False:
    node = open.dequeue()
    print("while start, node : ",node)
    node.showPath()
    
    if node.equal(end):
        print("end!\nPath : ",end = " ")
        node.showPath()
        print("cost : ",node.cost)
        print("number of generated nodes : ",end = " ")
        print(close.size())
        open.clear()
    else:
        close.enqueue(node)
        children = nodes[node.data] #dict
        print("children : ",children)
        for i in range(0,len(children['child'])):
            key = children['child'][i]
            print("key : ",key)
            cost = node.cost
            cost += children[key]
            print("before newNode, node.path : ", node.path)
            newNode = Node(key,node.path,cost)
            open.enqueue(newNode)

        # open.enqueue()
