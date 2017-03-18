from metrics import auc_score
from class_similarity import CommonNeighbors
from sampling_train_test_split import*





road = "e:/paper/dataset/com-dblp.ungraph.txt/com_dblp_ungraph.txt"
way = 'r'
fr = open(road,way)

nodepair_sets = train_test_split(fr,2,3000)
nodepair_set_train = nodepair_sets[0]
nodepair_set_test = nodepair_sets[1]
#print(nodepair_set_train)
#print(nodepair_set_test)


cn = CommonNeighbors()

vertex_dic = create_vertex(nodepair_set_train)

matrix_train = create_adjmatrix(nodepair_set_train,vertex_dic)
matrix_test = create_adjmatrix(nodepair_set_test,vertex_dic)


score = cn.fit(matrix_train)
auc = auc_score(score,matrix_train,matrix_test,'cc')

#print(vertex_dic)
print(matrix_train)
print(matrix_test)

print(score)

print('auc',auc)
