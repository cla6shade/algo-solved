n= int(input())
lst = list(map(int, input().split()))
dp = [_ for _ in lst]
for i in range(1, n):
    dp[i] = max(dp[i], dp[i] + dp[i-1])
print(max(dp))