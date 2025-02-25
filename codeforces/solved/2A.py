from sys import stdin
 
n = int(input())
 
final_scores = {}
running_scores = {}
winning_score = -100000000
winner = None
rounds = [0] * n 
 
for i in range(n):
    line = stdin.readline().split()
    name = line[0]
    score = int(line[1])
    rounds[i] = (name, score)    
    if name not in final_scores:
        final_scores[name] = 0
        running_scores[name] = 0
    final_scores[name] += score    

for score in final_scores.values():
    if score > winning_score:
        winning_score = score

for (name, score) in rounds:
    running_scores[name] += score
    if running_scores[name] >= winning_score and final_scores[name] == winning_score:
        winner = name
        break
 
print (winner)