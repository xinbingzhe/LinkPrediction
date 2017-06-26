
path = pathw = "E:/paper/dataset/dblp.xml/dblp_coauthor.txt"

fr = open(path,'r')

line = fr.readline()

i = 0

print("begin")
while line!='':
    re = line.strip('\n').split(',')

    year = int(re[0])

    if year<1000:
        print(re)
    line = fr.readline()

fr.close()