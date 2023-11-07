n, k = list(map(int, input().split()))
ns = list(range(1, n+1))

nextIndex = k - 1

perm = []
for i in range(n):
    while nextIndex > len(ns) - 1:
        nextIndex -= len(ns)
    perm.append(ns.pop(nextIndex))
    nextIndex += k - 1

ysputhString = ', '.join(list(map(str, perm)))
ysputhString = '<' + ysputhString.strip() + '>'
print(ysputhString)

