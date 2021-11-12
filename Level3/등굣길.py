# 등굣길
# https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for j, i in puddles:
        dp[i][j] = -1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:
                continue
            if i < n and dp[i + 1][j] != -1:
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % 1000000007
            if j < m and dp[i][j + 1] != -1:
                dp[i][j + 1] = (dp[i][j + 1] + dp[i][j]) % 1000000007
    answer = dp[n][m]                
    return answer