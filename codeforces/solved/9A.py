from sys import stdin

line = stdin.readline().split()
Y = int(line[0])
W = int(line[1])

res = max(Y, W)

if res == 1:
    print ("1/1")
elif res == 2:
    print ("5/6")
elif res == 3:
    print ("2/3")
elif res == 4:
    print ("1/2")
elif res == 5:
    print ("1/3")
else:    
    print ("1/6")