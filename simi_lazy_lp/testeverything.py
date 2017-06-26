'''def deco(func):
    print("before myfunc() called.")
    func()
    print("  after myfunc() called.")
    return func
 
def myfunc():
    print(" myfunc() called.")
 
myfunc = deco(myfunc)
def deco(func):
    print("before myfunc() called.")
    func()
    print("  after myfunc() called.")
    return func
 
@deco
def myfunc():
    print(" myfunc() called.")

#a = deco(myfunc)
myfunc()
def deco(func):
    def _deco():
        print("before myfunc() called.")
        func()
        print("  after myfunc() called.")
        # 不需要返回func，实际上应返回原函数的返回值
    return _deco
def abc(func):
    print("before abc.")
    func()
    print("  after myfunc() abc.")
    return func
@abc
@deco
def myfunc():
    print(" myfunc() called.")
    return 'ok'

abc(myfunc)

a = {1:12,2:23}
print(a.keys())
for i in a.keys():
    print(i)
print((1,2)==(2,1))'''
import networkx as nx
from heapq import*
G = nx.complete_graph(5)
preds = nx.adamic_adar_index(G, [(0, 1), (2, 3)])
#print(preds)
def a(l):
    s = {}
    for i in l:
        s[i] = 1
    return s
l = [0,1,2,3]
s = a(l)
print(a(l))
for i in s:
    print(i)

l = (x for x in range(5,0,-1))
print(l)
num = 0
for i in l:
    if num <2:
        print(i)
    else:
        break
    num += 1
print("next:")
for j in l:
    print(j)
#print("next:",next(l))
