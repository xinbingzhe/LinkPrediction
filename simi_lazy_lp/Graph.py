from vertex import vertex,adj_reservoir
from Nvertex import Nvertex,adj_reservoir
class Graph(object):
    """docstring for Graph"""
    def __init__(self,period,delta = 0.9,sigma = 1):
        """
            __vertex_dict:所有出现过的顶点的 字典
            __train_vertex_list:每轮训练的 顶点的字典的 集合列表

        """
        self.period = period
        self.__vertex_dict = {}
        self.__train_vertex_list = []
        self.delta = delta
        self.sigma = sigma
    def add_vertex(self,vertex):
        if vertex not in self.__vertex_dict:
            self.__vertex_dict[vertex.name] = vertex
    def get_vertex_dict(self):
        return self.__vertex_dict
    def get_vertex_dict_len(self):
        return len(self.__vertex_dict)
    def get_train_vertex_list(self):
        return self.__train_vertex_list
    def handle_train_set(self,train_set):
        """
            读入一个训练集顶点对，构建图，并生成一个顶点集用来生成测试集
            train_set :原始读取的一个数据集
            
                            
        """
        train_vertex_set = {}
        for pair in train_set:
            ts = pair[0]
            for v in pair[1:]: #keyi youhua
                if v not in self.__vertex_dict:
                    node = vertex(v,ts,self.period,self.delta,self.sigma)
                    self.add_vertex(node)
                if v not in train_vertex_set: 
                    train_vertex_set[v] = self.__vertex_dict[v]
                       
                        
                for u in pair[1:]:
                    if v!=u:
                        if u not in self.__vertex_dict:
                            nodeu = vertex(u,ts,self.period,self.delta,self.sigma) 
                            self.add_vertex(nodeu)
                        if u not in train_vertex_set:    
                            train_vertex_set[u] = self.__vertex_dict[u]  
                        self.__vertex_dict[v].adj_res.add_adjver(self.__vertex_dict[u]) #互相添加顶点到各自的邻接矩阵池中
                #print(self.__vertex_dict[v].adj_res.get_adjres())
        
        
        self.__train_vertex_list.append(train_vertex_set)

    def gen_test_pre(self,train_set,rate = 0.3):
        """
            generator 类型
            产生测试边
        """
        test_pair_set = []
        size = len(train_set)
        n = 0
        for pair in train_set:
            if n == size*rate:
                break
            for u in pair[1:]:
                for v in pair[1:]:
                    if u!=v:
                        if (u,v) not in test_pair_set and (v,u) not in test_pair_set:
                            test_pair_set.append((u,v))
                            yield (u,v)
        return test_pair_set


    def handle_train_set_normal(self,train_set):
        """
            
            读入一个训练集顶点对，构建图，并生成一个顶点集用来生成测试集
            train_set :原始读取的一个数据集
        

        """
        train_vertex_set = {}
        for pair in train_set:
            ts = pair[0]
            for v in pair[1:]: #keyi youhua
                if v not in self.__vertex_dict:
                    node = Nvertex(v,ts,self.period)
                    self.add_vertex(node)
                    if v not in train_vertex_set:    
                        train_vertex_set[v] = node    
                for u in pair[1:]:
                    if v!=u:
                        if u not in self.__vertex_dict:
                            nodeu = Nvertex(u,ts,self.period) 
                            self.add_vertex(nodeu)
                            if u not in train_vertex_set:    
                                train_vertex_set[u] = nodeu  
                        self.__vertex_dict[v].adj_res.add_adjver(self.__vertex_dict[u]) #互相添加顶点到各自的邻接矩阵池中
                #print(self.__vertex_dict[v].adj_res.get_adjres())
        
        
        self.__train_vertex_list.append(train_vertex_set)


"""--------------------------------"""
'''print("begin")
ts = "2011"


p = 20

node1 = vertex(1,ts,20)
node2 = vertex(2,ts,20)

g = Graph(p)
g.add_vertex(node1)
g.add_vertex(node2)
print(g.get_vertex_list)

node1.adj_res.add_adjver(node2)

print(g.get_vertex_list)'''

