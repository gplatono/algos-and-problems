sit = input()
maxteam = 0
for i in range(0, len(sit)):
    if i > 0 and sit[i] != sit[i-1] or i == 0:
        maxteam = 0
    maxteam += 1
    if maxteam == 7:
        print("YES")
        exit()

print("NO")