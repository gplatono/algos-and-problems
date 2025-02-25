from sys import stdin

n, m = [int(item) for item in stdin.readline().split()]

links = {}

for i in range(m):
    a, b = [int(item) for item in stdin.readline().split()]
    if a not in links:
        links[a] = {}
    if b not in links:
        links[b] = {}
    links[a][b] = 1
    links[b][a] = 1


for a in links.keys():
    for b in links[a].keys():
        for c in links[b].keys():
            if a != c:
                if c not in links[a].keys():
                    print ("NO")
                    exit()

print ("YES")