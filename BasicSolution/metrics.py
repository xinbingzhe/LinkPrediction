
def auc_score(matrix_score,matrix_test,matrix_train,n_compare=10):
    '''
            根据测试顶点的邻接矩阵，分出发生链接与没有发生链接的集合
            n_compare: int,'cc' ，计算auc比较次数，当该参数输入为int型时为比较次数，当输入为cc时以为Complete comparison，完全比较，默认参数为10
    '''
    import numpy as np
    import random

    if type(n_compare) == int:
        if len(matrix_test[0]) < 2:
            raise Exception("Invalid ndim!", train.ndim)
        elif len(matrix_test[0]) < 10:
            n_compare = len(matrix_test[0])
    else:
        if n_compare != 'cc':
            raise Exception("Invalid n_compare!", n_compare)

    unlinked_pair = []
    linked_pair = []

    #print(matrix_score[0][0])

    l = 1
    for i in range(0,len(matrix_test)):
        for j in range(0,l):
            if i != j and matrix_train[i][j]!=1: # 去掉训练集中已经存在的边
                if matrix_test[i][j] == 1:
                    linked_pair.append(matrix_score[i,j])
                elif matrix_test[i][j] == 0:
                    unlinked_pair.append(matrix_score[i,j])
                else:
                    raise Exception("Invalid connection!", matrix_test[i][j])
        l += 1

    auc = 0.0
    if n_compare == 'cc':
        frequency = min(len(unlinked_pair),len(linked_pair))
    else:
        frequency = n_compare
    for fre in range(0,frequency):
        unlinked_score = float(unlinked_pair[random.randint(0,frequency-1)])
        linked_score = float(linked_pair[random.randint(0,frequency-1)])
        if linked_score > unlinked_score:
            auc += 1.0
        elif linked_score == unlinked_score:
            auc += 0.5
    
    auc = auc/frequency
    
    return auc


