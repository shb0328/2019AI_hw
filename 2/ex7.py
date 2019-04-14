fn = {'a':30,'b':10,'c':100,'d':5}

res = min(fn.keys(),key = fn.get)
print(res)
print(type(res))

print('a' in fn)

print(fn)
del fn['a']
print(fn)

print(min([3,1,4,5,9]))
print(not fn)
fn.clear()
print(fn)

print(3)