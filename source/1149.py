n = int(input())
dp = [0]

for i in range(1, n + 1):
    if i == 1:
        dp.append(list(map(int, input().split())))  # 인덱스 1부터 append
        continue
    dp.append(list(map(int, input().split())))
    for j in range(3):
        if j == 0:
            dp[i][j] += min(dp[i-1][1], dp[i-1][2])
        elif j == 1:
            dp[i][j] += min(dp[i-1][0], dp[i-1][2])
        elif j == 2:
            dp[i][j] += min(dp[i-1][0], dp[i-1][1])
print(min(dp[n]))
