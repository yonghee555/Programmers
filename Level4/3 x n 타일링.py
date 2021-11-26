# 3 x n 타일링
# https://programmers.co.kr/learn/courses/30/lessons/12902

def solution(n):
    dp = [0] * (n + 1)
    dp[2] = 3
    dp[4] = 11
    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * 3 + 2
        for j in range(i - 4, 1, -2):
            dp[i] += dp[j] * 2
        dp[i] %= 1000000007
    answer = dp[n]
    return answer