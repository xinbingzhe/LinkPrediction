import numpy as np
import random


def train_test_split(fr,n_folds=2,edges = 'cr'):
    '''
        fr: 读取文件入口
        n_folds: 划分成的份数, 默认值为2,并且要大于2 且小于100,且小于edges
        edges : 边的数量 默认为'cr' 完全读完，最小为大于 2 的值
        文件默认以 \t 为分割符
        split n folds set 
        return nodepair_set[[[0,1],[2,3],,,],[],,,[]]

    '''
    if n_folds < 2:
        raise Exception("Invalid n_folds!", n_folds)
    if edges == 'cr':
        edges == float('inf')
    elif type(edges)!= str and edges < 2:
        raise Exception("Invalid edges!", edges)
    elif type(edges) == str and edges != 'cr':
        raise Exception("Invalid edges!", edges)

    if n_folds < 2:
        raise Exception("Invalid n_folds! shoud > 2",n_folds)
    elif n_folds > edges:
        raise Exception("Invalid n_folds! shoud < edges",n_folds)
    elif n_folds > 100:
        raise Exception("Invalid n_folds! shoud < 100",n_folds)

    nodepair_set = [[] for i in range(0,n_folds)]
    line = fr.readline()
    line = fr.readline().strip('\n').split('\t')
    i = 0
    while i < edges and line != '' :
        #print(line)
        nodepair_set[random.randint(0,n_folds-1)].append([int(line[0]),int(line[1])])
        line = fr.readline().strip('\n').split('\t')
        i += 1

    fr.close()
    return nodepair_set

def create_vertex(nodepair_set):
    '''
            nodepair_set : [[i,j],[i,k],......]
            return:vertex_set {i:0,j:1,k:2,...}
    '''
    # 产生vertex id 对应的字典 为了保证所有邻接矩阵所对应的的位置都一样
    vertex_set = {}
    num = 0
    for i in nodepair_set:
        if i[0] not in vertex_set:
            vertex_set[i[0]] = num
            num += 1
        if i[1] not in vertex_set:
            vertex_set[i[1]] = num
            num += 1
    return vertex_set

def create_adjmatrix(nodepair_set,vertex_set):
    '''
                nodepair_set  [ [i,j],[p,q],....]
                根据不同的顶点对，产生不同邻接矩阵
    '''
    init_matrix = np.zeros([len(vertex_set),len(vertex_set)])

    for pair in nodepair_set:
        if pair[0] in vertex_set and pair[1] in vertex_set:
            init_matrix[  vertex_set[pair[0]] ] [ vertex_set[pair[1]] ] = 1 
            init_matrix[  vertex_set[pair[1]] ] [ vertex_set[pair[0]] ] = 1 
    return init_matrix
    