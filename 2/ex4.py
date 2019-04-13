from pprint import pprint 

nodes = {'A':{'S':140,'B':30,'D':118,'Z':75}
		,'B':{}
		,'C':{'D':120,'P':138,'R':146}}


print(nodes)

print(nodes['A'])

child = sorted(nodes['A'].keys())

print(child)

nodes['A']['child'] = child

print(nodes)

print(nodes['A']['S'])

#예, 이거 안됩니다.
nodes2 = {'A':{'O':98}
		 ,'D':{'C':111,'A':118}}

# print(nodes & nodes2)
# print(nodes | nodes2)

ex = {}

print(ex is None)
print(ex == {})