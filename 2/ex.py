print("hello world")
#주석이다 ~!

number1 = 1
hello = "1 과 10 의 합 "
print(hello,number1 + 10,sep = ":",end = " ")
print("입니다.")

val = "^_^"
print("두 줄로 ",val,"\n입력하자!",sep = "*")

print(10**3)

#sort
number2 = 2

print(number1," ",number2)
number1,number2 = number2, number1
print(number1," ",number2)

print(type(number2),type(val))

#tuple
tup = (0,1,2,3,4,"gg")

print(tup,tup[3],tup[4:6],tup[5])
print("tuple 길이 : ",len(tup))
print("tuple 에 gg가 있는지 확인 : ", "gg" in tup)
print("tuple 에 gg가 없는지 확인 : ", "gg" not in tup)

tup2 = tup+tup
tup3 = tup*3

print(tup2,tup3)
print("tup3에 4가 몇개 ? ",tup3.count(4),"개")
print("tup3에 4의 첫번째 index는 ? ",tup3.index(4))

#set
se = {"tt",1,2,3}
print(type(se),se,len(se),'tt' in se)
se2 = {"qq",1,2,3,"hh"}
print(type(se2),se2,len(se2),'tt' not in se2)

se.add("hello")
print(se)
se.update([7,8,9])
print(se)
se.remove(7)
print(se)
se.discard("fdfdf")
print(se)
print("pop:",se.pop())
print(se)
#se.clear()
#print("clear:",se)

print("여기보세용")
print("se : ",se,"\nse2 : ",se2)
print(se & se2)
print(se | se2)

#list
lis = [1,2,3,"list","ss",11]
print(lis,"[3] :",lis[3],",[-0] :",lis[-0],",[-2] :",lis[-2],",[2:5] :",lis[2:5])
lis[3] = "hahaha"
print(lis)

lis2 = [100,300,"shb"]
print(lis+lis2, lis2*3)
lis2.append(999)
print(lis2,len(lis2),99 in lis2, 99 not in lis2)

lis3 = lis2.copy()
print(lis2,lis3)
lis3 = lis3*3
print("999몇개 ?",lis3.count(999))

print(lis)
lis.extend(lis2)
print(lis,"shb 의 index는? " ,lis.index("shb"))
lis.insert(8,20150439)
print(lis.pop(),lis)
print(lis.pop(8),lis)

print(lis3)
lis3.remove(999)
print(lis3)
lis3.reverse()
print(lis3)
#lis3.sort()
#print(lis3)

lis4 = [4,7,2,0,9,3,4]
lis4.sort()
print(lis4)

#dict
dic = {1:"one",2:"two",3:"three"}
print(dic,type(dic),len(dic))
print("1이 있니?",1 in dic,",one이 있니?","one" in dic,",잊지마! key검사야!")

print(dic[3])
dic[4] = "four"
print(dic)

dic2 = {"a":123,"b":"beee","c":1.5}
print(dic2,dic2["a"])
dic2["add"] = "추가한다!"
print(dic2)
dic2[1] = "추가한다!"
print(dic2)
dic2["a"]="바꾼다!"
print(dic2)
del dic2["b"] #삭제한다!
print(dic2)
#dic2.clear()
#print(dic2)

print(dic.items())
print(dic.keys())
print(dic.values())

print(dic,dic2,sep="\n")
dic.update(dic2)
print(dic)


#모듈
#import math
#print(dir(math))
#print(math.pow(2,3))
#일부만
#from math import pow,sqrt,trunc 
#print(pow(2,3))
#다른이름으로
# import math as ma
# print(ma.pow(2,3)

#함수
# def myfunc() :
# 	print("Hello World!")

# myfunc()

# def sum(x,y) :
# 	print(x+y)

# sum(11,13)

# x = int(input('x : '))
# y = int(input('y : '))
 
# sum(x,y)

# def returnSum(x,y) :
# 	z = x+y
# 	return z

# x = int(input('x : '))
# y = int(input('y : '))

# print(returnSum(x,y))