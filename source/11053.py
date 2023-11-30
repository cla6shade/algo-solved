n = int(input())
a = [0] + list(map(int, input().split()))

dp = [0] * 1001
dp[1] = a[1]
lens = [0] * 1001

maxValue= 1
for i in range(2, n+1):
    if a[i] < min(dp):
        dp[i] = a[i]
        lens[i] += 1

print(maxValue)
