import openpyxl
from pprint import pprint #pprint(dict) 시, key로 정렬해서 예쁘게 출력해준다. 단, dict는 원래 순서가 없음.

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


# 도시부터 B까지 직선거리 list로 추출
straights = []

for i in range(48, 51):
	for j in range(48, 58):
		if (i != 48 or j != 48):
			straight = s_sheet["B"+chr(i)+chr(j)].value
			if(straight is not None):
				straights.append(straight)

# {도시 : 직선거리, ... ,{}} dict로 만들기
citys = {}

for i in range(0, len(cityNames)):
	citys[cityNames[i]] = int(straights[i])

print("\n************************\n\ncitys with straight-line to B = \n")
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

# {key(출발 도시) : value{'도착도시':거리,...},...,{} } A->B
nodes1 = {}
for name in cityNames:
	nodes1[name] = {}

for i in range(48, 51):
 for j in range(48, 58):
  if (i != 48 or j != 48):
   A = d_sheet["A"+chr(i)+chr(j)].value
   B = d_sheet["B"+chr(i)+chr(j)].value
   Akey = (str(A))[0]
   Bkey = (str(B))[0]
   distance = d_sheet["C"+chr(i)+chr(j)].value
   if(A is not None):
    nodes1[Akey][Bkey] = distance # A->B



# B 열의 도시를 출발 key로.
# 도시 이름 list 뽑기.
cityNames.clear()
for i in range(48, 51):
	for j in range(48, 58):
		if (i != 48 or j != 48):
			city = d_sheet["B"+chr(i)+chr(j)].value
			if(city is not None):
				cityNames.append((str(city))[0])

# {key(출발 도시) : value{'도착도시':거리,...},...,{} } B->A
nodes2 = {}
for name in cityNames:
	nodes2[name] = {}

for i in range(48, 51):
 for j in range(48, 58):
  if (i != 48 or j != 48):
   A = d_sheet["A"+chr(i)+chr(j)].value
   B = d_sheet["B"+chr(i)+chr(j)].value
   Akey = (str(A))[0]
   Bkey = (str(B))[0]
   distance = d_sheet["C"+chr(i)+chr(j)].value
   if(Akey is not None):
    nodes2[Bkey][Akey] = distance # B->A


# d_sheet A->B 랑 B->A 합치기(최종)
nodes = {}
for name1 in nodes1.keys():
    # print(nodes1[name1])
    for name2 in nodes2.keys():
        if name1 == name2:
            nodes1[name1].update(nodes2[name2])
        else:
            nodes[name2] = nodes2[name2]

nodes.update(nodes1)

"""
알파벳 순서로 정렬된 자식 list를
{key(출발 도시) : value{'도착도시':거리,...,'child':[]},...,{} }
<- 'child':[]로 추가
"""

for name in nodes.keys():
    child = sorted(nodes[name].keys())
    nodes[name]['child'] = child

print("\n************************\n\nnodes with sorted child list = \n")
pprint(nodes)

# ================================================#

"""

BFS

"""

print("\n\n***** BFS *****\n\n")


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
        print("[",end="")
        for i in range(0,len(self.myList)):
            print(self.myList[i],end = " ")
        print("]")

# Node Class는 도시이름(data), 출발점부터 경로(path), 출발점부터 비용(cost)를 갖고 있다.
class Node:

    def __init__(self, data, path=[], cost=0):
        self.data = data
        self.path = path.copy()
        self.path.append(data)
        self.cost = cost

    def showPath(self):
        print(self.path)

    def equal(self, data):
        return self.data == data

    def __str__(self):
        return self.data


# BFS 는 right most!

start = 'T'
end = 'B'

open = Queue()
close = Queue()

startNode = Node(start)
open.enqueue(startNode)

while open.isEmpty() == False:
  print("open",end="")
  open.show();
  node = open.dequeue()
    
    # Check : Goal 인지 검사
  if node.equal(end):
    print("\n***** Result *****\n* Path : ",end = " ")
    node.showPath()
    print("* cost : ",node.cost)
    print("* number of generated nodes : ",end = " ")
    print(close.size())
    open.clear()
  else:
    print("close",end="")
    close.show();
    close.enqueue(node)
    children = nodes[node.data] #dict
    for i in range(0,len(children['child'])):
        key = children['child'][i]

        # Check : 왔던 경로에 key가 있었는지 검사
        if key not in node.path:
          cost = node.cost
          cost += children[key]
          newNode = Node(key,node.path,cost)
          open.enqueue(newNode)
