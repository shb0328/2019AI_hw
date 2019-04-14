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
                cityNames.append((str(city))[0]) # 도시 이름의 첫 대문자만 사용


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
                cityNames.append((str(city))[0]) # 도시 이름의 첫 대문자만 사용

# {key(출발 도시) : value{'도착도시':거리,...},...,{} } A->B
nodes1 = {}
for name in cityNames:
    nodes1[name] = {}

for i in range(48, 51):
 for j in range(48, 58):
  if (i != 48 or j != 48):
   A = d_sheet["A"+chr(i)+chr(j)].value
   B = d_sheet["B"+chr(i)+chr(j)].value
   Akey = (str(A))[0] # 도시 이름의 첫 대문자만 사용
   Bkey = (str(B))[0] # 도시 이름의 첫 대문자만 사용
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
                cityNames.append((str(city))[0]) # 도시 이름의 첫 대문자만 사용

# {key(출발 도시) : value{'도착도시':거리,...},...,{} } B->A
nodes2 = {}
for name in cityNames:
    nodes2[name] = {}

for i in range(48, 51):
 for j in range(48, 58):
  if (i != 48 or j != 48):
   A = d_sheet["A"+chr(i)+chr(j)].value
   B = d_sheet["B"+chr(i)+chr(j)].value
   Akey = (str(A))[0] # 도시 이름의 첫 대문자만 사용
   Bkey = (str(B))[0] # 도시 이름의 첫 대문자만 사용
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

Best First Search

"""

print("\n\n***** Best First Search *****\n\n")

class PriorityQ:

  def __init__(self):
    self.nodeList = list()
    self.fn = dict()

  def enqueue(self, node):
    self.nodeList.append(node)
    self.calFn(node)

  def dequeue(self):
    if self.isEmpty():
        return None
    key = self.fn[min(self.fn.keys())].pop(0) # fn 값이 같다면, FIFO
    res = self.nodeList # 어.. 잠시만
    return res

  def isEmpty(self):
    if not self.nodeList:
        return True
    return False

  def size(self):
    return len(self.nodeList)

  def clear(self):
    self.nodeList.clear()

  def show(self):
    print("[", end="")
    for i in range(0, len(self.nodeList)):
        print(self.nodeList[i], end = " ")
    print("]")

  # f(n) 계산해서 dict 타입 fn 에 { key/g(n)+h(n) : value/[도시이름 , ...](list)} 로 관리
  def calFn(self, node):
    gn = node.cost
    hn = citys[node.data]
    if gn+hn not in self.fn:
      self.fn[gn+hn] = [node.data]
    else:
      self.fn[gn+hn].append(node.data)
  # res = min(fn.keys(),key = fn.get)
    print(self.fn)


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


start = 'T'
end = 'B'

open = PriorityQ()
close = list()

startNode = Node(start)
open.enqueue(startNode)

while open.isEmpty() is False:
  print("open", end="")
  open.show()
  print("close",end="")
  close.show()

  node = open.dequeue()
  # Check : Goal 검사
  if node.equal(end):
    print("\n***** Result *****\n\n* Path : ", end = " ")
    node.showPath()
    print("* cost : ",node.cost)
    print("* number of generated nodes : ", end = " ")
    print(close.size())
    close.enqueue(node)
    print("\n******************\n\n")

