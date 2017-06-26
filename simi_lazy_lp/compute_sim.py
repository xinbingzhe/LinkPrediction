import time
from hash_ver import HashVertex
from Graph import Graph
from vertex import vertex,adj_reservoir
from streaming_samplling_train_test_split import undirect_temporal_ttsplit
from metrics import precision_gen
import networkx as nx

class compute_sim(object):
    """docstring for compute_sim"""
    
    def get_pairs_and_pre(self,train_set={}):
        """
            利用networkx 产生图 返回 图中的边集，预测集，以及图
        """
        if len(train_set)>0:
            G = nx.Graph()
            ed = []
            pre_ed = []
            for v in train_set:
                nv = v.name
                res_v = train_set[v].adj_res.get_sorted_adjres().keys()
                for u in res_v:
                    if (nv,u) not in ed and (u,nv) not in ed: 
                        ed.append((nv,u))
                G.add_edges_from(e)
                for i in train_set:
                    if v != i:
                        ni = i.name
                        if (nv,ni) not in pre_ed and (ni,nv) not in pre_ed:
                            pre_ed.append((nv,ni))
            return ed,pre_ed,G
    
    def CN_qs(self,train_set={}):
        """
            train_set: 顶点
        """
        start_time = time.time()
        cu = 0
        cv = 0
        #train_set_pair_score = []
        train_set_pair_score = {}
        setime = 0
        for v in train_set:
            #print(train_set[v])
            st1 =  time.time()
            res_v = train_set[v].adj_res.get_sorted_adjres()
            et1 = time.time()
            setime = setime + et1 - st1
            score_vu = 0 
            for u in train_set:
                if v != u:
                    st2 = time.time()
                    res_u = train_set[u].adj_res.get_sorted_adjres()# 这一步会导致时间增加
                    et2 = time.time()
                    setime = setime + et1 - st1
                    #print(v,":",res_v)
                    #print(u,":",res_u)
                    if (v,u) not in train_set_pair_score and (u,v) not in train_set_pair_score:
                        """计算过的就不计算了，快速计算共同邻居"""
                        
                        while cu < len(res_u) and cv < len(res_v):
                            if res_u[cu] == res_v[cv]:
                                score_uvi = train_set[v].weights_dic[res_v[cv]] + train_set[u].weights_dic[res_u[cu]] # score 
                                score_vu += score_uvi
                                cu += 1
                                cv += 1
                            elif res_u[cu] > res_v[cv]:
                                cv += 1
                            elif res_u[cu] < res_v[cv]:
                                cu += 1
                        cu = 0
                        cv = 0
                        if score_vu != 0:
                            #train_set_pair_score.append((u,v))
                            #yield (v,u,round(score_vu,3))
                            train_set_pair_score[(u,v)] =  round(score_vu,3)
                            score_vu = 0
        end_time = time.time()
        #del train_set_pair_score
        print(end_time-start_time-setime)
        return train_set_pair_score

    def CN(self,train_set={}):
        start_time = time.time()
        train_set_pair_score = {}
        for v in train_set:
            #print(train_set[v])
            res_v = train_set[v].adj_res.get_adjres()

            score_vu = 0 
            for u in train_set:
                if v != u:
                    res_u = train_set[u].adj_res.get_adjres()
                    #print(v,":",res_v)
                    #print(u,":",res_u)
                    if (v,u) not in train_set_pair_score and (u,v) not in train_set_pair_score:
                       
                        for i in res_v:
                            for j in res_u:
                                if i == j:
                                    score_vu += 1        
                        if score_vu != 0:
                            #train_set_pair_score.append((u,v))
                            yield (v,u,round(score_vu,3))
                            train_set_pair_score[(u,v)] =  round(score_vu,3)
                            score_vu = 0
        end_time = time.time()
        print(end_time-start_time)
        #del train_set_pair_score
        #return train_set_pair_score

    def Jaccard(self,train_set={}):
        start_time = time.time()
        train_set_pair_score = []
        for v in train_set:
            #print(train_set[v])
            res_v = train_set[v].adj_res.get_adjres()

            score_vu = 0 
            for u in train_set:
                if v != u:
                    res_u = train_set[u].adj_res.get_adjres()
                    #print(v,":",res_v)
                    #print(u,":",res_u)
                    if (v,u) not in train_set_pair_score and (u,v) not in train_set_pair_score:
                        
                        for i in res_v:
                            for j in res_u:
                                if i == j:
                                    score_vu += 1        
                        if score_vu != 0:
                            score_vu = score_vu/(len(res_v)+len(res_u)-score_vu)
                            train_set_pair_score.append((u,v))
                            yield (v,u,round(score_vu,3))
                            score_vu = 0
        end_time = time.time()
        print(end_time-start_time)
        del train_set_pair_score
        #return train_set_pair_score
    def AA(self,train_set={}):
        """
        """
        start_time = time.time()
        #train_set_pair_score = {}
        e,pre_ed,G = self.get_pairs_and_pre(train_set)
        pre_re = nx.adamic_adar_index(G, pre_ed)


        print(end_time-start_time)
        return pre_re


    def increment_cp(self,fr,graph,CP_MODE,rounds=1,edges = 5000):
        """
                实现增量计算
                fr：文件读取
                graph：图对象
                CP_MODE:compute_sim对象的计算函数
                rounds：计算轮数， 
                edges：读取的数据量
        """
        nodepair_set = undirect_temporal_ttsplit(fr,n_folds=rounds+1,edges=edges)
        g = graph
        
        print(CP_MODE)
        r = 0
        if CP_MODE != self.CN_qs:
            while r < rounds:
                g.handle_train_set_normal(nodepair_set[r])
                train_dict = g.get_train_vertex_list()
                v_dict = g.get_vertex_dict()
                train_pair_score = CP_MODE(train_dict[r])
                print("round",r)
                test = g.gen_test_pre(nodepair_set[r+1],rate=0.2)
                #print(test)
                pre = precision(train_pair_score,test,L=1000)
                #print(train_set_pair_score)
                print("precision",pre)
                r = r+1
        else:
            while r < rounds:
                g.handle_train_set(nodepair_set[r])
                train_dict = g.get_train_vertex_list()
                v_dict = g.get_vertex_dict()
                train_pair_score = CP_MODE(train_dict[r])
                print("round",r)
                test = g.gen_test_pre(nodepair_set[r+1],rate=0.2)
                #print(test)
                pre = precision(train_pair_score,test,L=1000)
                #print(train_set_pair_score)
                print("precision",pre)
                r = r+1


