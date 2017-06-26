
class vertex(object):
    """docstring fos vertex"""
    def __init__(self,name,ts,period,delta = 0.9,sigma = 1):
        self.name = name
        self.timestamp = int(ts)
        self.period = period
        self.weights_dic = {}
        self.delta = delta
        self.sigma = sigma
        self.adj_res = adj_reservoir(period,self.weights_dic,int(ts),self.delta,self.sigma)
        


class adj_reservoir(object):
    """docstring for adj_reservoir"""
    def __init__(self,period,weights_dic,start_ts,delta = 0.9,sigma = 1):
        self.period = period
        self.__start_ts = start_ts
        self.weights_dic = weights_dic
        #print(self.weight_dic)
        self.__adjres ={}
        self.delta = delta
        self.sigma = sigma
        self.__sorted_adjres = []
    def add_adjver(self,vertex):
        if vertex.timestamp - self.__start_ts <= self.period:
            self.__adjres[vertex.name] = vertex.timestamp
            #print(self.weights_dic)
            self.add_weights_dic(vertex)
        else:
            self.update_start_ts_weights_dic(vertex)
    def set_start_ts(self,ts):
        self.__start_ts = int(ts)
    def get_start_ts(self):
        return self.__start_ts
    def add_weights_dic(self,adjver):
        """
            权重变大
        """
        if adjver in self.weights_dic:
            self.weights_dic[adjver.name] = self.weights_dic[adjver.name] + self.delta
        else:         
            self.weights_dic[adjver.name] = self.delta
    def plus_weights_dic(self):
        """
            权重变小
        """
        for adj in self.weights_dic:
            if adj not in self.__adjres:
                self.weights_dic[adj] = self.weights_dic[adj]*self.sigma
    def update_start_ts_weights_dic(self,vertex):
        """ 
            更新邻接矩阵池 
            更新self.__start_ts
            更新权重矩阵
        """
        self.__adjres[vertex.name] = vertex.timestamp
        self.add_weights_dic(vertex)
        sorted_adjres = sorted(self.__adjres.items(), key=lambda d:d[1])
        for v in sorted_adjres:
            if vertex.timestamp - v[1] > self.period:
                self.__adjres.pop(v[0])
                sorted_adjres.pop(0)
        self.__start_ts = sorted_adjres[0][1]
        self.plus_weights_dic()
    def get_adjres(self):
        return self.__adjres
    def get_adj_len(self):
        """ 获取元素个数 """
        return len(self.__adjres)
    def get_sorted_adjres(self):
        return sorted(self.__adjres.keys())

'''ts = "2011"


period = 20

node1 = vertex(1,ts,20)
node2 = vertex(2,ts,20)

#node1.adj_res.set_start_ts("2005")
node1.adj_res.add_adjver(node2)

print(node1.adj_res.get_adj_len())'''

