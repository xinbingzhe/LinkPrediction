from hash_ver import HashVertex

def direct_temporal_ttsplit(fr,n_folds=2,train_rate = 0.8,edges = 'cr'):
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
        edges = float('inf')
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

    while i < edges and line != [''] :
        #print(line)
    
        nodepair_set[random.randint(0,n_folds-1)].append([int(line[0]),int(line[1])])
        line = fr.readline().strip('\n').split('\t')
       
       
        i += 1

    fr.close()
    return nodepair_set


def undirect_temporal_ttsplit(fr,n_folds=2,edges = 'cr'):
    '''
        fr: 读取文件入口
        n_folds: 划分成的份数, 默认值为2,并且要大于2 且小于100,且小于edges
        fold_size: 每个划分的数据量，数据条数
        edges : 边的数量 默认为'cr' 完全读完，最小为大于 2 的值
        文件默认以 \t 为分割符
        split n folds set 
        return: nodepair_set[[[t1,0,1],[t2,2,3],,,]  ,,,[],,,[]]
                n_folds个训练集，每个集合都是时间戳与哈希过的顶点对

    '''
    
    fold_size = 0
    if n_folds < 2:
        raise Exception("Invalid n_folds!", n_folds)
    if edges == 'cr':
        edges = float('inf')
        fold_size = 100000
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
    
    if edges != 'cr':
        fold_size = edges/n_folds

    print("fold_size:",fold_size)
    """init set"""
    nodepair_set = [[] for i in range(0,n_folds)]
    line = fr.readline().strip('\n').split(',')
    i = 0
    set_num = 0
    hash_ver = HashVertex()
    #print(line)
    NUM = 0
    while i < edges and line != [] :
        ts = int(line[0])
        line.pop(0)
        NUM += len(line)
        #print(line)
        nodepair_set[set_num].append([ts])
        for l in line:
            nodepair_set[set_num][-1].append(hash_ver.hash(l))
        #print(nodepair_set[set_num])
        if len(nodepair_set[set_num]) >= fold_size and set_num< n_folds:
            set_num += 1

        line = fr.readline().strip('\n').split(',')
        #print("line:",line)
        i += 1

    fr.close()
    print(hash_ver.get_hash_dict_len())
    print(NUM)
    return nodepair_set

'''path = 'E:/paper/dataset/dblp.xml/dblp_coauthor.txt'
fr = open(path,'r')

nodepair_set = undirect_temporal_ttsplit(fr,n_folds=2,edges=10)

print(nodepair_set)'''