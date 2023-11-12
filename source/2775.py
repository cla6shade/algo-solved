cases = int(input())
res = []
for _ in range(cases):
    n = int(input())
    k = int(input())
    apart = [i for i in range(0, k + 1)]

    for i in range(1, n+1): # 0층 제외, 1층부터 n층까지
        for j in range(1, k+1): # 1호~k호. 층수만큼 1~k호까지 더해주면 최종 결과와 같음.
            apart[j] += apart[j-1]
    res.append(apart[k])

for r in res:
    print(r)
