n = int(input())

users = {}

for i in range(n):
    name = input()
    if name not in users:
        print("OK")
        users[name] = 1
    else:        
        print(name + str(users[name]))
        users[name] += 1