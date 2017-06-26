from hash_ver import HashVertex
from Graph import Graph
from vertex import vertex,adj_reservoir
from compute_sim import compute_sim
from streaming_samplling_train_test_split import undirect_temporal_ttsplit
from metrics import precision_gen,preWOge
import time
path = 'E:/paper/dataset/dblp.xml/dblp_coauthor.txt'
fr = open(path,'r')

'''nodepair_set = undirect_temporal_ttsplit(fr,n_folds=2,edges=10000)

#print(nodepair_set)

p = 30

g = Graph(p)

g.handle_train_set(nodepair_set[0])

train_dict = g.get_train_vertex_list()
#print(train_dict[0])
v_dict = g.get_vertex_dict()
#print(v_dict.keys())

    #print(i,adj)

sim = compute_sim()
train_pair_score = sim.CN_qs(train_dict[0])

test = g.gen_test_pre(nodepair_set[1])
#print(test)
pre = precision(train_pair_score,test,L=100)
#print(train_set_pair_score)
print("precision",pre)'''

fr = ''
fr = open(path,'r')
nodepair_set = undirect_temporal_ttsplit(fr,n_folds=2,edges=20000)
p = 30
gN = Graph(p)
gN.handle_train_set_normal(nodepair_set[0])
train_dict = gN.get_train_vertex_list()
v_dict = gN.get_vertex_dict()
sim = compute_sim()
print("CN")
train_pair_score = sim.CN(train_dict[0])

#print(train_dict[0])
print("-----------------------------")
#print(list(train_pair_score))
test = gN.gen_test_pre(nodepair_set[1],rate=0.3)
#print(nodepair_set[1])
#print(list(test))
#print(test)
start_time = time.time()
pre = preWOge(train_pair_score,test,L=100)
end_time = time.time()
print("pre-time",end_time-start_time)
#print(train_set_pair_score)
print("precision",pre)
'''train_pair_score_JA = sim.Jaccard(train_dict[0])
pre = precision(train_pair_score_JA,test,L=1000)
print("Jaccard")
print("precision",pre)'''
'''p = 30
gN = Graph(p)

sim = compute_sim()

sim.increment_cp(fr,gN,CP_MODE=sim.CN_qs, rounds=14, edges= 9000)
'''
