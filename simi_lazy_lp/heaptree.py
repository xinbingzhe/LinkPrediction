from heapq import*
class heapNode(object):
    """docstring for heapNode"""
    def __init__(self,name,value):
        self.name = name
        self.value = value

class heapTree():

    def initTree(self,l):
        """
            l 为 name value 对
        """
        hTree = []
        for name,value in l:
            n = heapNode(name,value)
            hTree.append(n)
        return hTree
    def heapsort(self,hTree):
        """
            对 顶点进行排序,小顶堆
        """
        n = len(hTree)
        for e in range(int(n/2-1),-1,-1):
            self.heapfixdown(hTree,e)
            
    def heapfixdown(self,hTree,i):
        """

            堆得的向下调整，i为开始节点的位置

        """
        n = len(hTree)
        j = int(2*i+1)
        while j < n:
            fv = hTree[i].value
            if j+1 < n and hTree[j].value > hTree[j+1].value:
                j += 1
            sv = hTree[j].value
            if fv <= sv:
                break
            hTree[j],hTree[i] = hTree[i],hTree[j]
            i = j
            j = int(2*i+1)

    def heapdelete(self,hTree):
        """
            为了删除树头结点，小顶堆的删除
        """
        n = len(hTree)
        hTree[0] = hTree[n-1]
        hTree.pop()
        self.heapfixdown(hTree,0)
            

    def heapinsert(self,hTree,hNode):
        """
                插入小顶堆
        """
        hTree.append(hNode)
        i = len(hTree)-1
        j = int(i/2-1)
        while j > 0:
            fv = hTree[j].value
            sv = hTree[i].value
            if fv < sv:
                break
            hTree[j],hTree[i] = hTree[i],hTree[j]
            i = j
            j = int(i/2-1)

    def heapupdate(self,hTree,hNode):
        """
            维持k 大小的小顶堆
        """
        if hNode.value > hTree[0].value:
            self.heapdelete(hTree)
            self.heapinsert(hTree,hNode)

'''l = [('a',2),('v',90),('g',89),('f',234),('j',12),('sd',1),('sf',0)]

ht = heapTree()
hTree = ht.initTree(l)
ht.heapsort(hTree)

for i in hTree:
    print(i.value)
print(":::::::")
a = heapNode('sfds',987)
ht.heapupdate(hTree,a)
for i in hTree:
    print(i.value)'''