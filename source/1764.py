n, m = list(map(int, input().split()))
d = {}
for i in range(n):
    str = input()
    d[str] = True
dbs = []
for j in range(m):
    str = input()
    if str in d:
        dbs.append(str)
dbs.sort()
print(len(dbs))

for d in dbs:
    print(d)