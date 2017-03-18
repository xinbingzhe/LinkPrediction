import numpy as np
import random
import pandas as pd
from sampling_train_test_split import*
import numpy.matlib

class  similarity(object):
    """docstring for  similarity"""
    
    def fit(self,train_adj):
        "矩阵维度大于1"
        train = np.matrix(train_adj)
        if train.ndim < 2:
            raise Exception("Invalid ndim!", train.ndim)
        if train.size < 2:
            raise Exception("Invalid size!", train.size)
        if train.shape[0] != train.shape[1]:
            raise Exception("Invalid shape!", train.shape)


class CommonNeighbors(similarity):
    """
            CommonNeighbors 求交集
    """
    def fit(self,train_adj):
        similarity.fit(self,train_adj)
        train_adj = np.matrix(train_adj)

        return train_adj * train_adj

class Jaccard(similarity):
    """
            两顶点邻居的交集与并集之比
    """
    def fit(self,train_adj):
        similarity.fit(self,train_adj)
        train_adj = np.matrix(train_adj)
        numerator =  train_adj * train_adj
        deg0 = np.matlib.repmat(train_adj.sum(0),len(train_adj),1)
        deg1 = np.matlib.repmat(train_adj.sum(1),1,len(train_adj))
        denominator = deg0 + deg1 - numerator
        sim = numerator/denominator
        sim[np.isnan(sim)] = 0
        sim[np.isinf(sim)] = 0
        return sim
        #denominator = 




'''
test

nodepair_set = [[0,1],[0,2],[1,2],[1,5],[1,3],[3,4],[3,5],[3,4],[2,5],[2,0]]

Ja = Jaccard()
vertex_dic = create_vertex(nodepair_set)

matrix_train = create_adjmatrix(nodepair_set,vertex_dic)

print(vertex_dic)
print(matrix_train)

print(Ja.fit(matrix_train))
'''
