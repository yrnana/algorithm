dp = [[0, 0, 0, 0] for i in range(100001)]


def solution(land):
    answer = 0
    dp[0] = land[0].copy()
    r, c = len(land), 4  # 3, 4
    for i in range(1, r):
        for j in range(4):
            for k in range(4):
                if j != k:
                    dp[i][j] = max(dp[i][j], land[i][j] + dp[i - 1][k])
    for i in range(4):
        answer = max(answer, dp[r - 1][i])
    return answer


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))  # 16
