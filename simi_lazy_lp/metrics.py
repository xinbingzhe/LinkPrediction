from collections import OrderedDict

from heaptree import*
def precision_gen(train_pair_score,test_pair_set,L = 20):

    print("metrics")
    pair_list = []
    Lpair = []
    num = 0
    for u,v,s in train_pair_score:
        if num < L:
            pair_list.append(((u,v),s))
        else:
            break
        num += 1
    ht = heapTree()
    hTree = ht.initTree(pair_list)
    ht.heapsort(hTree)
    for u,v,s in train_pair_score:
        a = heapNode((u,v),s)
        ht.heapupdate(hTree,a)

    for l in hTree:
        Lpair.append((l.name,l.value))
    m = 0
    print(Lpair)
    test = []
    for t in test_pair_set:
        test.append(t)
        if t in Lpair:
            m += 1
    print("m",m)
    #print(test)
    precision = round(m/L,3)
    #print(precision)
    return precision

def preWOge(train_pair_score,test_pair_set,L = 20):
    L_dict = {}
    for i in train_pair_score:
        L_dict[(i[0],i[1])]=i[2]
    sortld = sorted(L_dict.items(),key = lambda item:item[1],reverse = True)
    #print(sortld)
    Lmax = []
    num = 0
    for j in sortld:
        if num == L:
            break
        num+=1
        Lmax.append(j[0])
       
    #print(Lmax)
    m = 0
    test = []
    for t in test_pair_set:
        test.append(t)
        if t in Lmax or (t[1],t[0]) in Lmax:
            m += 1
    #print(test)
    precision = round(m/L,3)
    return precision