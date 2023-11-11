n = int(input())
score = [0] * 301

stairs = [0]
for i in range(n):
    stairs.append(int(input()))

score[1] = stairs[1]
if n >= 2:
    score[2] = stairs[1] + stairs[2]
if n >= 3:
    score[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

for i in range(4, n+1):
    score[i] = max(stairs[i] + stairs[i-1] + score[i-3], stairs[i] + score[i-2])
print(score[n])
