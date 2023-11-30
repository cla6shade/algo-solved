count = int(input())
res = []


def ncr(n, r):
    if n == r:
        return 1
    if n == r + 1 or r == 1:
        return n
    ret = 1
    for i in range(n - r + 1, n + 1):
        ret *= i
    for j in range(1, r + 1):
        ret //= j
    return int(ret)


for _ in range(count):
    r, n = list(map(int, input().split()))
    print(ncr(n, r))
