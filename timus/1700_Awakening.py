import sys

features = {}
objects = {}

inp = sys.stdin.readlines()
n = int(inp[0])

for i in range(1, n+1):
    line = inp[i].split()
    obj = line[0][:-1]
    objects[obj] = []
    for feat in line[1:]:
        if feat not in features:
            features[feat] = {}
        features[feat][obj] = 1
        objects[obj].append(feat)
    objects[obj].sort()

m = int(inp[n+1])

for i in range(n+2, n+2+m):
    objs = inp[i].split()
    fs = []
    for f in objects[objs[0]]:
        flag = True
        for o in objs[1:]:
            if o not in features[f]:
                flag = False
                break
        
        if flag == True:
            fs.append(f)

    if fs != []:
        print (" ".join(fs))
    else:
        print ("No solution.")