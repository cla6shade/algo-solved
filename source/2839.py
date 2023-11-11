n = int(input())
db = [-1] * 5001

for i in range(3, n + 1):
    if i == 3 or i == 5:
        db[i] = 1
        continue
    if db[i - 3] == -1 and db[i - 5] == -1:
        continue
    elif db[i - 3] == -1:
        db[i] = db[i - 5] + 1
    elif db[i - 5] == -1:
        db[i] = db[i - 3] + 1
    else:
        db[i] = min(db[i - 3] + 1, db[i - 5] + 1)
print(db[n])
