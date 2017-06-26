
class Nvertex(object):
    """
        docstring fos vertex 普通顶点

    """
    def __init__(self,name,ts,period):
        self.name = name
        self.timestamp = int(ts)
        self.period = period

        self.adj_res = adj_reservoir(period,int(ts))
        


class adj_reservoir(object):
    """docstring for adj_reservoir"""
    def __init__(self,period,start_ts):
        self.period = period
        self.__start_ts = start_ts
        #print(self.weight_dic)
        self.__adjres ={}
    def add_adjver(self,vertex):
        if vertex.timestamp - self.__start_ts <= self.period:
            self.__adjres[vertex.name] = vertex.timestamp
            #print(self.weights_dic)
        else:
            self.update_start_ts_dic(vertex)
    def set_start_ts(self,ts):
        self.__start_ts = int(ts)
    def get_start_ts(self):
        return self.__start_ts
    def update_start_ts_dic(self,vertex):
        """ 
            更新邻接矩阵池 
            更新self.__start_ts
        """
        self.__adjres[vertex.name] = vertex.timestamp
        sorted_adjres = sorted(self.__adjres.items(), key=lambda d:d[1])
        for v in sorted_adjres:
            if vertex.timestamp - v[1] > self.period:
                self.__adjres.pop(v[0])
                sorted_adjres.pop(0)
        self.__start_ts = sorted_adjres[0][1]
    def get_adjres(self):
        return self.__adjres
    def get_adj_len(self):
        """ 获取元素个数 """
        return len(self.__adjres)


'''ts = "2011"


period = 20

node1 = vertex(1,ts,20)
node2 = vertex(2,ts,20)

#node1.adj_res.set_start_ts("2005")
node1.adj_res.add_adjver(node2)

print(node1.adj_res.get_adj_len())'''

